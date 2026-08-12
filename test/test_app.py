from Backend.app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
