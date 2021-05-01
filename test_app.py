import os
import json
import pytest

import app


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client
    [os.remove(os.path.join(app.DATA_DIR, file)) for file in os.listdir(app.DATA_DIR)]


def test_create_metric_value(client):
    response = client.post(
        "/metric/test_key",
        json={
            "value": 42,
        },
    )
    assert response.status_code == 200
    assert json.loads(response.data) == {}


def test_metric_sum(client):
    response = client.get("/metric/test_key/sum")
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "value": 0,
    }


def test_create_metric_value_and_metric_sum(client):
    response = client.post(
        "/metric/test_key",
        json={
            "value": 42,
        },
    )
    response = client.get("/metric/test_key/sum")
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "value": 42,
    }
