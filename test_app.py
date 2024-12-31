import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_task(client):
    response = client.post('/api/tasks', 
                          json={'task': 'Test task'})
    assert response.status_code == 201
    
    # Verify task was added
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert 'Test task' in response.json 