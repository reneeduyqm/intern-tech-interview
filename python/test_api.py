"""Tests for api.py."""

from copy import deepcopy
import api

import pytest

@pytest.fixture
def TEST_DB():
    db = deepcopy(api.construct_db())
    return db


def test_get_all(TEST_DB):
    """Test the users GET endpoint succeeds when retrieving all users."""
    user, status = api.get()
    assert user == TEST_DB
    assert status == 200


def test_get_one(TEST_DB):
    """Test the users GET endpoint succeeds when retrieving one user."""
    user_id = next(iter(TEST_DB))
    user, status = api.get(user_id=user_id)
    assert user == TEST_DB[user_id]
    assert status == 200


def test_get_fail():
    """Test the users GET endpoint fails when the user is not found."""
    msg, status = api.get(user_id="does_not_exist")
    assert "not found" in msg
    assert status == 404


def test_post_success(TEST_DB):
    """Test the users POST endpoint succeeds when creating a new user."""
    orig_user_count = len(TEST_DB)
    body = dict(name="Waxillium", email="wax@brandosando.net", friends=[], age=25)
    user_id, status = api.post(body=body)
    assert user_id in api.DB
    assert len(api.DB) == orig_user_count + 1
    assert status == 201


@pytest.mark.parametrize(
    'body,status_code,message',
    [
        ({}, 400, "body"),
        (dict(email="wax@brandosando.net"), 400, "name"),
        (dict(name="Wax"), 400, "email"),
        (dict(email="wax@brandosando.net", name="Wax"), 400, "friends"),
        (dict(email="wax@brandosando.net", name="Wax", friends=[], age="20"), 400, "an integer"),
        (dict(email="wax@brandosando", name="Wax", friends=[]), 400, "incorrect form"),
        (dict(email="wax@brandosando.net", name="Wax", friends=["bad name"]), 400, "not present"),
    ]
)
def test_post_fail(body, status_code, message):
    """Test the users POST endpoint fails with invalid data."""
    msg, status = api.post(body=body)
    assert message in msg
    assert status_code == status


def test_put_success(TEST_DB):
    """Test the users PUT endpoint succeeds when creating a new user."""
    api.DB = TEST_DB
    body = dict(name="Siri", email="sir@brandosando.net", friends=[])
    user_id = next(iter(TEST_DB))
    msg, status = api.put(_id=user_id, body=body)
    assert msg is None
    assert status == 204
    assert body == api.DB[user_id]


@pytest.mark.parametrize(
    '_id_index,body,status_code,message',
    [
        (0, {}, 400, "body"),
        (0, dict(email="wax@brandosando.net"), 400, "name"),
        (0, dict(name="Wax"), 400, "email"),
        (0, dict(email="wax@brandosando.net", name="Wax"), 400, "friends"),
        (
            None,
            dict(name="Siri", email="sir@brandosando.net", friends=[]),
            404,
            "not found"
        ),
        (
            0,
            dict(email="wax@brandosando.net", name="Wax", friends=[], age="20"),
            400,
            "an integer"
        ),
        (
            0,
            dict(email="wax@brandosando", name="Wax", friends=[]),
            400,
            "incorrect form"
        ),
        (
            0,
            dict(email="wax@brandosando.net", name="Wax", friends=["bad name"]),
            400,
            "not present"
        ),
    ]
)
def test_put_fail(TEST_DB, _id_index, body, status_code, message):
    """Test the users PUT endpoint fails with invalid data."""
    if _id_index is None:
        _id = "bad_id"
    else:
        _id = list(TEST_DB.keys())[_id_index]
    msg, status = api.put(_id=_id, body=body)
    assert message in msg
    assert status == status_code

def test_delete_success(TEST_DB):
    """Test the users DELETE endpoint succeeds."""
    api.DB = TEST_DB
    orig_user_count = len(TEST_DB)
    user_id = next(iter(TEST_DB))
    msg, status = api.delete(_id=user_id)
    assert msg is None
    assert status == 204
    assert len(api.DB) == orig_user_count - 1

@pytest.mark.parametrize(
    '_id,status_code,message',
    [
        (None, 404, "not found"),
    ]
)
def test_user_delete_fail(_id, status_code, message):
    """Test the users delete endpoint fails."""
    msg, status = api.delete(_id=_id)
    assert message in msg
    assert status == status_code
