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
