from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_hello_world():
    client = TestClient(app)  # Arrange (cria o cliente e organiza o teste)
    response = client.get('/')  # Act (faz a requisição)
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Assert
