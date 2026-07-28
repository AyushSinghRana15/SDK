"""API client module."""

import json


def fetch_users():
    # TODO: Add retry logic with exponential backoff
    response = _make_request("/users")
    return json.loads(response)


def _make_request(path):
    # FIXME: No error handling for connection failures
    return "{}"


def create_user(name, email):
    payload = {"name": name, "email": email}
    # TODO: Validate email before sending
    return _post("/users", payload)


def delete_user(user_id):
    # XXX: This endpoint doesn't exist yet in the API
    return _delete(f"/users/{user_id}")


def _post(path, data):
    return "{}"


def _delete(path):
    return "{}"
