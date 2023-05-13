import json

from api import api


def test_packages():
    with api.test_client() as client:
        # sending a request and then loading the JSON response
        req = client.get("/packages/mnl")
        data = json.loads(req.data)

        # comparing the response with the expected results
        assert all(
            [
                req.status_code == 200,
                data["name"] == "monolith",
                data["authors"] == ["Retcy"],
                data["slug_name"] == "mnl",
                data["desc"] == "This is a test",
            ]
        )


def test_home():
    with api.test_client() as client:
        req = client.get("/")

        # sending a request to '/' and then comparing the response to the encoded string
        assert all(
            [
                req.status_code == 200,
                req.data == bytearray("👀 Curiosity kills the 🐱 cat!".encode()),
            ]
        )
