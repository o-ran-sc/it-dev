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

from http import HTTPStatus

def test_onboard_get(client):
    response = client.get('/api/v1/onboard')
    assert response.status_code == HTTPStatus.OK, 'Improper status code'
    assert response.json == {'status': 'OK'}, 'Improper response'



def test_onboard_post(client):
    data = {
        "config-file.json": {"chart_name": "test", "version": "1.1.1", "non-tests": "nontest"},
        "schema.json": {"required": ["non-tests"]}
    }
    url = '/api/v1/onboard'

    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.CREATED, 'Improper status code'
    assert response.content_type == 'application/json', 'Content type error'
    assert response.json == {'status': 'Created'}, 'Onboard failed'
