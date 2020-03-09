import logging

from flask_restplus import Resource
from HelmManager.api.api_server import api
from HelmManager.api.models.response_models import status_message_model, error_message_model
from HelmManager.repo_manager.repo_manager import repo_manager

log = logging.getLogger(__name__)
ns = api.namespace('health', description='health check')


@ns.route('')
class HealthCheck(Resource):

    @api.response(200, 'Health check OK', status_message_model)
    @api.response(500, 'Helm manager is not ready', error_message_model)
    def get(self):
        """
        Returns the health condition of the xApp Helm chart manager.
        """
        if not repo_manager.is_repo_ready():
            return {'errors': {'source': "HelmManager main server",
                               "error message": "Cannot connect to local helm repo."}, "status": "Service not ready." }, 500
        return {'status': 'OK'}, 200
