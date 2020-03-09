from http import HTTPStatus


def test_health(client):
    response = client.get('/api/v1/health')
    assert response.status_code == HTTPStatus.OK, 'Health check failed'
    assert response.json == {'status': 'OK'}, 'Improper response'