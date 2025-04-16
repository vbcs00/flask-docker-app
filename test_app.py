from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Hello Dockerized Flask App!" in response.data

def test_about():
    tester = app.test_client()
    response = tester.get("/about")
    assert response.status_code == 200
    assert b"About Us" in response.data

def test_greet():
    tester = app.test_client()
    response = tester.get("/greet/Alice")
    assert response.status_code == 200
    assert b"Hello, Alice!" in response.data

def test_404():
    tester = app.test_client()
    response = tester.get ("/nonexistent")
    assert response.status_code == 404
