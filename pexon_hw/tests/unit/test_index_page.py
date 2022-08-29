
from urllib import response
from app import app
 

def test_index_page():
    flask_app= app

    with flask_app.test_client() as test_client:
        response= test_client.get('/')
        assert response.status_code== 200
        assert b"Pexonian" in response.data
  