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

import logging
import json
from jsonschema import ValidationError, SchemaError
from jsonschema import validate, Draft7Validator
from HelmManager.helm_controller.xApp_builder import xApp, xAppError
from HelmManager import settings
from HelmManager.repo_manager.repo_manager import requests_retry_session, repo_manager


log = logging.getLogger(__name__)


def onboard(config_file, schema_file):

    if not repo_manager.is_repo_ready():
        return {'errors': {'source': "HelmManager main server",
                           "error message": "Cannot connect to local helm repo."},
                "status": "Service not ready."}, 500

    try:
        Draft7Validator.check_schema(schema_file)
        validate(config_file, schema_file)
    except ValidationError as err:
        log.debug(err.message)
        return_message = {"errors": {"source": "config-file.json", "error message": err.message},
                          "status": "Input payload validation failed"}
        return return_message, 400
    except SchemaError as err:
        log.debug(err.message)
        return_message = {"errors": {"source": "schema.json", "error message": err.message},
                          "status": "Input payload validation failed"}
        return return_message, 400

    try:
        xapp = xApp(config_file, schema_file)
        xapp.package_chart()
        xapp.distribute_chart()
    except xAppError as err:
        print(type(err))
        log.error(str(err))
        return_message = {"errors": {"source": "xApp_builder", "error message": str(err)},
                          "status": "xApp onboarding failed"}
        return return_message, err.status_code
    return {'status': 'Created'}, 201


def download_config_and_schema(config_file_url, schema_url):

    if not repo_manager.is_repo_ready():
        return {'errors': {'source': "HelmManager main server",
                           "error message": "Cannot connect to local helm repo."},
                "status": "Service not ready."}, 500, None, None

    session = requests_retry_session()
    try:
        response = session.get(config_file_url, timeout=settings.HTTP_TIME_OUT)
    except Exception as err:
        log.debug(err.message)
        return_message = {"errors": {"source": "config-file.json", "error message": err.message},
                          "status": "Downloading config-file.json failed"}
        return return_message, 500, None, None
    else:
        if response.status_code != 200:
            error_message = "Wrong response code. " + str(response.status_code) + " " + response.content.decode("utf-8")
            log.debug(error_message)
            return_message = {"errors": {"source": "config-file.json", "error message": error_message},
                              "status": "Downloading config-file.json failed"}
            return return_message, 500, None, None
        config_file = json.loads(response.content)

    try:
        response = session.get(schema_url, timeout=settings.HTTP_TIME_OUT)
    except Exception as err:
        log.debug(err.message)
        return_message = {"errors": {"source": "schema.json", "error message": err.message},
                          "status": "Downloading schema.json failed"}
        return return_message, 500, None, None
    else:
        if response.status_code != 200:
            error_message = "Wrong response code. " + str(response.status_code) + " " + response.content.decode("utf-8")
            log.debug(error_message)
            return_message = {"errors": {"source": "schema.json", "error message": error_message},
                              "status": "Downloading schema.json failed"}
            return return_message, 500, None, None
        schema_file = json.loads(response.content)

    return {'status': 'OK'}, 200, config_file, schema_file
