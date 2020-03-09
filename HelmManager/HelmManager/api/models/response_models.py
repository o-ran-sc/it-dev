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

from flask_restplus import fields
from HelmManager.api.api_server import api

error_message_model = api.model('error_message', {
    'errors': fields.Nested(
        api.model('source', {
            'source': fields.String(description='source of the error', required=True),
            'error message':fields.String(description='source of the error', required=True)}), required=True),
    'status': fields.String(description='http response message', required=True),
})

status_message_model = api.model('status', {
    'status': fields.String(description='status of the service', required=True)
})
