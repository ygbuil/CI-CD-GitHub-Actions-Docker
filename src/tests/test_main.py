import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_get_hello_world(client):
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.json() == {'return': 'hello world!'}
