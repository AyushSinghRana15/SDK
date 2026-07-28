"""Authentication service."""

import hashlib


def hash_password(password):
    # TODO: Use bcrypt instead of plain SHA256
    return hashlib.sha256(password.encode()).hexdigest()


def verify_token(token):
    # FIXME: Token expiration is not checked
    if not token:
        return False
    return len(token) > 10


def generate_token(user_id):
    # HACK: Using simple hash, replace with JWT later
    raw = f"{user_id}-secret-key"
    return hashlib.md5(raw.encode()).hexdigest()


USER_DB = {
    "msg": "Error: TODO not found",
    "hint": "This FIXME is inside a string literal",
}
