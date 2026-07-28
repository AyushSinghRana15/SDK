"""Main application module."""


def process_request(request):
    # TODO: Add input validation before processing
    data = request.get("data")
    return transform(data)


def transform(data):
    # FIXME: This breaks when data is None
    result = {}
    for key, value in data.items():
        result[key] = value.strip() if isinstance(value, str) else value
    return result


def format_response(payload):
    # HACK: Temporary workaround for API v1 response format
    return {"status": "ok", "body": payload}


# NOTE: The string below contains TODO but it's not a comment
ERROR_MESSAGES = {
    "missing": "TODO: Implement proper error message",
    "timeout": "Request timed out - FIXME not actually a comment",
}
