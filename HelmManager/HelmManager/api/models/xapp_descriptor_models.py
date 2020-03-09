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

from flask_restplus import fields
from HelmManager.api.api_server import api

xapp_descriptor_post = api.model('descriptor', {
    'config-file.json': fields.Nested(
        api.model('config', {
            'chart_name': fields.String(description='Name of the xApp chart', required=True),
            'version': fields.String(description='Version of the xApp chart', required=True,
                                     pattern='^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'),
        }), required=True),
    'schema.json': fields.Raw(description='Schema file body', required=True),
})


xapp_descriptor_download_post = api.model('descriptor_remote', {
    'config-file.json_url': fields.Url(description='URL to download the config-file.json file',  absolute=True, required=True),
    'schema.json_url': fields.Url(description='URL to download the schema.json file',  absolute=True, required=True),
})

