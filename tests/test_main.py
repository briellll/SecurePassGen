from http import HTTPStatus

from fastapi.testclient import TestClient

from securepassgen.main import app

client = TestClient(app)


def test_endpoint_create_passwords_ok():
    payload = {'length': 14, 'add_number': True, 'add_symbol': True}

    response = client.post('/gerar-senha', json=payload)

    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert 'password_created' in data
    assert isinstance(data['password_created'], str)
    assert len(data['password_created']) == payload['length']
    assert data['parameter'] == payload
