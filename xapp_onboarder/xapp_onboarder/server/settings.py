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

import os

# Flask settings
FLASK_SERVER_NAME = os.environ.get('FLASK_SERVER_NAME') or '0.0.0.0:8888'
FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = os.environ.get('RESTPLUS_SWAGGER_UI_DOC_EXPANSION') or 'list'
RESTPLUS_VALIDATE = os.environ.get('RESTPLUS_VALIDATE') or True
RESTPLUS_MASK_SWAGGER = os.environ.get('RESTPLUS_MASK_SWAGGER') or False
RESTPLUS_ERROR_404_HELP = os.environ.get('RESTPLUS_ERROR_404_HELP') or False

# temp settings
CHART_WORKSPACE_PATH = os.environ.get('CHART_WORKSPACE_PATH') or '/tmp/xapp_onboarder'
CHART_REPO_URL = os.environ.get('CHART_REPO_URL') or 'http://0.0.0.0:8888'
HTTP_TIME_OUT = os.environ.get('HTTP_TIME_OUT') or 10
HTTP_RETRY = os.environ.get('HTTP_RETRY') or 3
ALLOW_REDEPLOY = os.environ.get('ALLOW_REDEPLOY') or True
CHART_WORKSPACE_SIZE = os.environ.get('CHART_WORKSPACE_SIZE') or '500 MB'

# Environment variables that will be passed into xApp
DBAAS_MASTER_NAME = os.environ.get('DBAAS_MASTER_NAME')
DBAAS_SERVICE_HOST = os.environ.get('DBAAS_SERVICE_HOST')
DBAAS_SERVICE_SENTINEL_PORT = os.environ.get('DBAAS_SERVICE_SENTINEL_PORT')
DBAAS_SERVICE_PORT = os.environ.get('DBAAS_SERVICE_PORT')
