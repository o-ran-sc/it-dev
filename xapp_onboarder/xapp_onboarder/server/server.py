from xapp_onboarder.server import settings
import logging
from flask import Flask, Blueprint
from xapp_onboarder.api.api_reference import api
from xapp_onboarder.api.endpoints.onboard_ep import ns as onboard_ns
from xapp_onboarder.api.endpoints.health_check_ep import ns as health_check_ns
from xapp_onboarder.api.endpoints.charts_ep import ns as charts_ns
from xapp_onboarder.helm_controller.artifacts_manager import start_trim_thread

log = logging.getLogger(__name__)

class server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
        self.app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
        self.app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
        self.app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
        self.app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP




        self.api = api
        self.api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
        self.api.init_app(self.api_bp)

        self.api.add_namespace(onboard_ns)
        self.api.add_namespace(health_check_ns)
        self.api.add_namespace(charts_ns)
        self.app.register_blueprint(self.api_bp)
        start_trim_thread()


    def run(self):

        log.info('>>>>> Starting development xapp_onboarder at http://{}/api/v1/ <<<<<'.format(self.app.config['SERVER_NAME']))
        self.app.run(debug=settings.FLASK_DEBUG)