################################################################################
#   Copyright (c) 2019 AT&T Intellectual Property.                             #
#   Copyright (c) 2019 Nokia.                                                  #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
################################################################################

import logging
import yaml
import json
import os
import subprocess
import shutil
import re
import copy
from HelmManager import settings
from HelmManager.repo_manager.repo_manager import repo_manager, RepoManagerError
from pkg_resources import resource_filename

log = logging.getLogger(__name__)


def indent(text, amount, ch=' '):
    padding = amount * ch
    return ''.join(padding + line for line in text.splitlines(True))


class xAppError(Exception):
    def __init__(self, message, status_code):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.status_code = status_code


class xApp():
    def __init__(self, config_file, schema_file):
        self.config_file = config_file
        self.schema_file = schema_file

        if 'chart_name' not in self.config_file:
            raise xAppError(
                "xApp chart name not found. (Caused by: config-file.json does not contain chart_name attribute.)", 500)

        if 'version' not in self.config_file:
            raise xAppError(
                "xApp chart version not found. (Caused by: config-file.json does not contain version attribute.)", 500)

        self.chart_name = self.config_file['chart_name']
        self.chart_version = self.config_file['version']

        self.configmap_config_json_file = copy.deepcopy(self.config_file)

        self.chart_workspace_path = settings.CHART_WORKSPACE_PATH + '/' + self.chart_name + '-' + self.chart_version


        if os.path.exists(self.chart_workspace_path):
            shutil.rmtree(self.chart_workspace_path)

        os.makedirs(self.chart_workspace_path)
        shutil.copytree(resource_filename( 'HelmManager', 'resources/xapp-std'), self.chart_workspace_path + '/' + self.chart_name)

#        with open(self.chart_workspace_path + '/' + self.chart_name + '/values.yaml', 'r') as inputfile:
#            self.values_yaml = yaml.load(inputfile, Loader=yaml.FullLoader)




    def recursive_converte_config_file(self, node_list=list()):
        current_node = self.configmap_config_json_file
        helm_value_path = '.Values'
        for node in node_list:
            current_node = current_node.get(node)
            helm_value_path = helm_value_path + '.' + node

        if type(current_node) is not dict:
            raise TypeError("Recursive write was called on a leaf node.")

        for item in current_node.keys():
            if type(current_node.get(item)) is not dict:
                current_node[item] = '{{ '+ helm_value_path +'.'+ item + ' | toJson }}'
            else:
                new_node_list = node_list.copy()
                new_node_list.append(item)
                self.recursive_converte_config_file(new_node_list)



    def append_config_to_config_map(self):
        with open(self.chart_workspace_path + '/' + self.chart_name + '/templates/appconfig.yaml', 'a') as outputfile:
            self.recursive_converte_config_file()
            config_file_json_text = json.dumps(self.configmap_config_json_file, indent=4)
            indented_config_text = indent(config_file_json_text, 4)
            indented_config_text = re.sub(r"\"{{", '{{', indented_config_text)
            indented_config_text = re.sub(r"}}\"", '}}', indented_config_text)
            outputfile.write("  config-file.json: |\n")
            outputfile.write(indented_config_text)
            outputfile.write("\n  schema.json: |\n")
            schema_json = json.dumps(self.schema_file, indent=4)
            indented_schema_text = indent(schema_json, 4)
            outputfile.write(indented_schema_text)


    def add_probes_to_deployment(self):
        with open(self.chart_workspace_path + '/' + self.chart_name + '/templates/deployment.yaml', 'a') as outputfile:

            for probes in ['readinessProbe', 'livenessProbe']:
                if self.configmap_config_json_file.get(probes):
                    probe_definition = self.configmap_config_json_file.get(probes)
                    probe_definition_yaml = yaml.dump(probe_definition)
                    indented_probe_definition_yaml = indent(probe_definition_yaml, 12)
                    indented_probe_definition_yaml = re.sub(r" \| toJson", '', indented_probe_definition_yaml)
                    indented_probe_definition_yaml = re.sub(r"'", '', indented_probe_definition_yaml)
                    outputfile.write("          "+probes+":\n")
                    outputfile.write(indented_probe_definition_yaml)



    def append_config_to_values_yaml(self):
        with open(self.chart_workspace_path + '/' + self.chart_name + '/values.yaml', 'a') as outputfile:
            yaml.dump(self.config_file, outputfile, default_flow_style=False)


    def append_env_to_config_map(self):
        with open(self.chart_workspace_path + '/' + self.chart_name + '/templates/appenv.yaml', 'a') as outputfile:
            append = {}
            if settings.DBAAS_MASTER_NAME:
                master_name = settings.DBAAS_MASTER_NAME
                service_host = settings.DBAAS_SERVICE_HOST
                sentinel_port = settings.DBAAS_SERVICE_SENTINEL_PORT
                if not service_host:
                    raise xAppError(
                        "Internal failure. Cannot find environment variable 'DBAAS_SERVICE_HOST'. (Caused by: Misconfiguration of helm manager deployment)", 500)
                if not sentinel_port:
                    raise xAppError(
                        "Internal failure. Cannot find environment variable 'DBAAS_SERVICE_SENTINEL_PORT'. (Caused by: Misconfiguration of helm manager deployment)", 500)

                append['DBAAS_MASTER_NAME'] = master_name
                append['DBAAS_SERVICE_HOST'] = service_host
                append['DBAAS_SERVICE_SENTINEL_PORT'] = sentinel_port
            elif settings.DBAAS_SERVICE_HOST:
                service_host = settings.DBAAS_SERVICE_HOST
                service_port = settings.DBAAS_SERVICE_PORT
                if not service_port:
                    raise xAppError(
                        "Internal failure. Cannot find environment variable 'DBAAS_SERVICE_PORT'. (Caused by: Misconfiguration of helm manager deployment)", 500)
                append['DBAAS_SERVICE_HOST'] = service_host
                append['DBAAS_SERVICE_PORT'] = service_port
            else:
                raise xAppError(
                    "Internal failure. Cannot find environment variable 'DBAAS_SERVICE_HOST' or 'DBAAS_MASTER_NAME'. (Caused by: Misconfiguration of helm manager deployment)",
                    500)
            output_yaml = yaml.dump(append)
            indented_output_yaml = indent(output_yaml, 2)
            outputfile.write(indented_output_yaml)


    def change_chart_name_version(self):
        with open(self.chart_workspace_path + '/' + self.chart_name + '/Chart.yaml', 'r') as inputfile:
            self.chart_yaml = yaml.load(inputfile, Loader=yaml.FullLoader)
            self.chart_yaml['version'] = self.chart_version
            self.chart_yaml['name'] = self.chart_name

        with open(self.chart_workspace_path + '/' + self.chart_name + '/Chart.yaml', 'w') as outputfile:
            yaml.dump(self.chart_yaml, outputfile, default_flow_style=False)


    def helm_lint(self):
        try:
            process = subprocess.run(["helm", "lint", self.chart_workspace_path + "/" + self.chart_name], capture_output=True, check=True)

        except OSError as err:
            raise xAppError(
                "xApp " + self.chart_name + '-' + self.chart_version + " helm lint failed. (Caused by: " + str(
                    err) + ")", 500)
        except subprocess.CalledProcessError as err:
            raise xAppError(
                "xApp " + self.chart_name + '-' + self.chart_version + " helm lint failed. (Caused by: " +
                err.stderr.decode("utf-8") +  "\n" + err.stdout.decode("utf-8") + ")", 400)

    def package_chart(self):
        self.append_config_to_config_map()
        self.append_config_to_values_yaml()
        self.append_env_to_config_map()
        self.add_probes_to_deployment()
        self.change_chart_name_version()
        self.helm_lint()
        try:
            process = subprocess.run(["helm", "package", self.chart_workspace_path + "/" + self.chart_name, "-d"
                               ,self.chart_workspace_path], capture_output=True, check=True)

        except OSError as err:
                raise xAppError("xApp "+ self.chart_name+'-'+self.chart_version +" packaging failed. (Caused by: "+str(err) +")", 500)
        except subprocess.CalledProcessError as err:
            raise xAppError(
                "xApp " + self.chart_name + '-' + self.chart_version + " packaging failed. (Caused by: " +
                    err.stderr.decode("utf-8") + ")", 500)



    def distribute_chart(self):
        try:
            repo_manager.upload_chart(self)
        except RepoManagerError as err:
            raise xAppError( "xApp " + self.chart_name + '-' + self.chart_version + " distribution failed. (Caused by: " + str(err) + ")" , err.status_code)

