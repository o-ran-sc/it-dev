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