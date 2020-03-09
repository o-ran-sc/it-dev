import logging

from flask_restplus import Api
from HelmManager import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='RIC Helm Manager API',
          description='APIs to manage the xApp helm charts')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


