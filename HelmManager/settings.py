import os

# Flask settings
FLASK_SERVER_NAME = os.environ.get('FLASK_SERVER_NAME') or '0.0.0.0:8888'
FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = os.environ.get('RESTPLUS_SWAGGER_UI_DOC_EXPANSION') or 'list'
RESTPLUS_VALIDATE = os.environ.get('RESTPLUS_VALIDATE') or True
RESTPLUS_MASK_SWAGGER = os.environ.get('RESTPLUS_MASK_SWAGGER') or False
RESTPLUS_ERROR_404_HELP = os.environ.get('RESTPLUS_ERROR_404_HELP') or False

# HelmManager settings
CHART_WORKSPACE_PATH = os.environ.get('CHART_WORKSPACE_PATH') or '/tmp/helmmanager'
CHART_REPO_URL = os.environ.get('CHART_REPO_URL') or 'http://127.0.0.1:27015'
HTTP_TIME_OUT = os.environ.get('HTTP_TIME_OUT') or 10
HTTP_RETRY = os.environ.get('HTTP_RETRY') or 3
ALLOW_REDEPLOY = os.environ.get('ALLOW_REDEPLOY') or True
CHART_WORKSPACE_SIZE = os.environ.get('CHART_WORKSPACE_SIZE') or '500 MB'

# Environment variables that will be passed into xApp
DBAAS_MASTER_NAME = os.environ.get('DBAAS_MASTER_NAME')
DBAAS_SERVICE_HOST = os.environ.get('DBAAS_SERVICE_HOST')
DBAAS_SERVICE_SENTINEL_PORT = os.environ.get('DBAAS_SERVICE_SENTINEL_PORT')
DBAAS_SERVICE_PORT = os.environ.get('DBAAS_SERVICE_PORT')