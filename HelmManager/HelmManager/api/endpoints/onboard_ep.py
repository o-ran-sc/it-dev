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
from flask import request
from flask_restplus import Resource
from HelmManager.api.models import xapp_descriptor_models
from HelmManager.api.api_server import api
from HelmManager.api.models.response_models import status_message_model, error_message_model
from HelmManager.repo_manager.repo_manager import repo_manager
from HelmManager.api.onboard import onboard, download_config_and_schema

log = logging.getLogger(__name__)
ns = api.namespace('onboard', description='onboard xApps')


@ns.route('')
class OnboardxApps(Resource):

    # @api.response(200, 'Everything is fine')
    # @api.response(500, 'Helm manager is not ready')
    # def get(self):
    #     """
    #     Return a list of xApp that have been onboarded and their versions.
    #     """
    #     if not repo_manager.is_repo_ready():
    #         return {'status': 'not ready'}, 500
    #     return {'status': 'OK'}, 200

    @api.response(201, 'xApp onboard successfully.', status_message_model)
    @api.response(400, 'xApp descriptor format error', error_message_model)
    @api.response(500, 'Helm manager is not ready', error_message_model)
    @api.expect(xapp_descriptor_models.xapp_descriptor_post, validate=True)
    def post(self):
        """
        Onboard xApp
        """
        config_file = request.json.get('config-file.json')
        schema_file = request.json.get('schema.json')

        return onboard(config_file, schema_file)


@ns.route('/download')
class OnboardxAppsDownload(Resource):

    @api.response(201, 'xApp onboard successfully.', status_message_model)
    @api.response(400, 'xApp descriptor format error', error_message_model)
    @api.response(500, 'Helm manager is not ready', error_message_model)
    @api.expect(xapp_descriptor_models.xapp_descriptor_download_post, validate=True)
    def post(self):
        """
        Onboard xApp with remote xApp descriptor
        """

        config_file_url = request.json.get('config-file.json_url')
        schema_url = request.json.get('schema.json_url')

        message, status, config_file, schema_file = download_config_and_schema(config_file_url, schema_url)

        if status != 200:
            return message, status
        else:
            return onboard(config_file, schema_file)
