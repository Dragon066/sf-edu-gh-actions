from starlette.testclient import TestClient


def test_hello_endpoint(test_client: TestClient):
    response = test_client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_item(test_client: TestClient):
    response = test_client.get("/item/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "foo", "price": 19.99, "is_offer": True}


def test_add_item(test_client: TestClient):
    response = test_client.post(
        "/item", json={"name": "foo", "price": 29.99, "is_offer": False}
    )
    assert response.status_code == 200
    response_list = test_client.get("/items")
    assert response_list.json() == [
        {"name": "foo", "price": 29.99, "is_offer": False}
    ]
