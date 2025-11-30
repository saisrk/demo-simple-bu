import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_greet_with_name(client):
    """Test that greeting works with valid input"""
    response = client.post('/greet', json={'name': 'Alice'})
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, Alice!'}

def test_greet_without_name(client):
    """Test that greeting handles missing name gracefully - THIS WILL FAIL"""
    response = client.post('/greet', json={})
    # Expected: 400 Bad Request with error message
    # Actual: 500 Internal Server Error due to KeyError
    assert response.status_code == 400
    assert 'error' in response.json
