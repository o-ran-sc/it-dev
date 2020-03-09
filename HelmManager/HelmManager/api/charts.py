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

import logging
import io
import tarfile
from HelmManager.repo_manager.repo_manager import repo_manager, RepoManagerError


log = logging.getLogger(__name__)


def get_charts_list(xapp_chart_name=''):

    if not repo_manager.is_repo_ready():
        return {'errors': {'source': "HelmManager main server",
                           "error message": "Cannot connect to local helm repo."},
                "status": "Service not ready."}, 500
    try:
        content = repo_manager.get_xapp_list(xapp_chart_name=xapp_chart_name)
    except RepoManagerError as err:
        log.error(str(err))
        return_message = {"errors": {"source": "charts_fetcher", "error message": str(err)},
                          "status": "Fetching helm chart list failed"}
        return return_message, err.status_code
    return content, 200


def download_chart_package(xapp_chart_name, version):

    if not repo_manager.is_repo_ready():
        return {'errors': {'source': "HelmManager main server",
                           "error message": "Cannot connect to local helm repo."},
                "status": "Service not ready."}, 500

    try:
        content = repo_manager.download_xapp_chart(xapp_chart_name=xapp_chart_name, version=version)
    except RepoManagerError as err:
        log.error(str(err))
        return_message = {"errors": {"source": "charts_fetcher", "error message": str(err)},
                          "status": "Artifact downloading failed"}
        return return_message, err.status_code

    return content, 200


def download_values_yaml(xapp_chart_name, version):

    content, status = download_chart_package(xapp_chart_name=xapp_chart_name, version=version)

    if status != 200:
        return content, status

    file_stream = io.BytesIO(content)

    with tarfile.open(fileobj=file_stream) as tar:
        values_yaml_file = tar.extractfile(xapp_chart_name + '/values.yaml')
        return_response = values_yaml_file.read()

    return return_response, 200

