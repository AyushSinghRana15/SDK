"""Tests for helpers."""

from src.utils.helpers import sanitize_input, validate_email


def test_sanitize_input():
    # TODO: Add more edge cases for special characters
    assert sanitize_input("hello world!") == "helloworld"
    assert sanitize_input("test@123") == "test123"


def test_validate_email():
    # FIXME: Fails for .museum TLD
    assert validate_email("user@example.com") is True
    assert validate_email("not-an-email") is False


# Message shown when tests fail: "Check the TODO items in the output"
FAIL_HINT = "Scan found 0 FIXME issues"
