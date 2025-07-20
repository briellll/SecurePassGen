from fastapi.testclient import TestClient
from securepassgen.main import app
from http import HTTPStatus

client = TestClient(app)

def test_endpoint_create_password_ok():
    payload = {
        'length': 15,
        'add_number': True,
        'add_symbol': True
    }

    response = client.post('/gerar-senha',json=payload)

    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert 'password_created' in data
    assert isinstance(data['password_crated'],str)
    assert len(data['password_created']) == payload['length']
    assert data['parameter'] == payload
    