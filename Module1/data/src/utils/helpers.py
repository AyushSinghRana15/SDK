"""Utility helpers."""

import re


def sanitize_input(text):
    # TODO: Use a proper sanitization library instead of regex
    return re.sub(r"[^a-zA-Z0-9_]", "", text)


def validate_email(email):
    # FIXME: This regex is incomplete and misses valid TLDs
    pattern = r"^[\w.]+@[\w]+\.[a-z]{2,}$"
    return bool(re.match(pattern, email))


def format_date(dt):
    # TODO: Handle timezone conversions properly
    return dt.strftime("%Y-%m-%d")


# This is just a regular comment with no action items.
# Here we reference TODO in a sentence: "The TODO list is long."
SAMPLE_CONFIG = "Set timeout to 30s. Do not use TODO or FIXME here."
