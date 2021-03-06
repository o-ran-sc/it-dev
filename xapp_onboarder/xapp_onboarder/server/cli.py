################################################################################
#   Copyright (c) 2020 AT&T Intellectual Property.                             #
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


import fire
import json
import os
import pkg_resources
import logging.config

from xapp_onboarder.api.charts import get_charts_list, download_chart_package, download_values_yaml
from xapp_onboarder.repo_manager.repo_manager import repo_manager
from xapp_onboarder.api.onboard import onboard, download_config_and_schema_and_onboard

log = logging.getLogger(__name__)


class cli():
    """This is the cli tool for xapp_onboarder."""

    def get_charts_list(self, xapp_chart_name=''):
        """Get the list of all onboarded xApps. To show all version of an xApp, use --xapp_chart_name to
        specify the name."""
        message, status = get_charts_list(xapp_chart_name=xapp_chart_name)

        return json.dumps(message, indent=4, sort_keys=True)

    def download_helm_chart(self, xapp_chart_name, version, output_path="."):
        """Download the helm chart package of an xApp. Specify xApp name with --xapp_chart_name, version with
        --version. Optionally use --output_path to specify the path to save the file."""
        content, status = download_chart_package(xapp_chart_name=xapp_chart_name, version=version)

        if status != 200:
            return json.dumps(content, indent=4, sort_keys=True)

        try:
            if os.path.isabs(output_path):
                path = output_path + '/' + xapp_chart_name + '-' + version + '.tgz'
            else:
                path = os.getcwd() + '/' + output_path + '/' + xapp_chart_name + '-' + version + '.tgz'

            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))

            with open(path, 'wb') as outputfile:
                outputfile.write(content)
        except Exception as err:
            return err
        return {"status": "OK"}

    def download_values_yaml(self, xapp_chart_name, version, output_path="."):
        """Download the values.yaml file that can be used to override parameters at runtime. Specify xApp name with
        --xapp_chart_name, version with --version. Optionally use --output_path to specify the path to save the file.
        """
        content, status = download_values_yaml(xapp_chart_name=xapp_chart_name, version=version)

        if status != 200:
            return json.dumps(content, indent=4, sort_keys=True)

        try:
            if os.path.isabs(output_path):
                path = output_path + '/values.yaml'
            else:
                path = os.getcwd() + '/' + output_path + '/values.yaml'

            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))

            with open(path, 'wb') as outputfile:
                outputfile.write(content)
        except Exception as err:
            return err
        return {"status": "OK"}

    def health(self):
        """Health check. If xapp onboarder is not ready, it return false."""
        return repo_manager.is_repo_ready()

    def onboard(self, config_file_path, shcema_file_path):
        """Onboard an xApp with local descriptor files. Use --config_file_path to specify the path to
        config-file.json file, --shcema_file_path to specify the path to schema.json file. """
        try:
            with open(config_file_path, 'r') as inputfile:
                config_file = json.load(inputfile)

            with open(shcema_file_path, 'r') as inputfile:
                schema_file = json.load(inputfile)

        except Exception as err:
            return err

        message, status = onboard(config_file, schema_file)
        return json.dumps(message, indent=4, sort_keys=True)

    def download_and_onboard(self, config_file_url, schema_file_url):
        """Onboard an xApp with URLs pointing to the xApp descriptor files. Use --config_file_url to specify the
        config-file.json URL, --schema_file_url to specify the schema.json URL. """
        message, status = download_config_and_schema_and_onboard(config_file_url, schema_file_url)
        return json.dumps(message, indent=4, sort_keys=True)

def run():
    logger_config = pkg_resources.resource_filename("xapp_onboarder", 'logging.conf')
    logging.config.fileConfig(logger_config)
    fire.Fire(cli(), name='xapp_onboarder')

if __name__ == "__main__":

    run()
