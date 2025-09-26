from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # Arrange

    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Olá Mundo!"}  # Assert


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "email": "alice@example.com",
                "username": "alice",
            },
        ]
    }

def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "alice_updated",
            "email": "alice_updated@example.com",
            "password": "new_secret"
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "alice_updated",
        "email": "alice_updated@example.com",
    }