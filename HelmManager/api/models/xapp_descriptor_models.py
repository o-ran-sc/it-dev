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

