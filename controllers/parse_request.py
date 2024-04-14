from flask import request


def get_request_data():
    """
    Get keys & values from request (Note that this method should parse requests with content type "application/x-www-form-urlencoded")
    """
    if request.content_type:
        if request.content_type.startswith('application/x-www-form-urlencoded'):
            data = request.form.to_dict()
        else:
            data = {}
        return data
    else:
        return {}
