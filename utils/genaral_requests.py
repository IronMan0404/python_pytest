""" This file contains all type of requests"""
__author__ = "Bhargava Batchu"

import requests


# Get Request
def get_response_from_api(url, header):
    """
    This function will return the response
    :param url:
    :param header:
    :return: response
    """
    response = requests.get(url=url, json=header)
    try:
        assert response.status_code == 200, "expected status code is 200, but we got: {}".format(response.status_code)
        return response
    except AssertionError:
        raise ValueError(response.content)


# Post Request
def post_request_to_api(url, headers, data):
    """
    This Function can handle the post request
    :param url: endpoint
    :param headers:
    :param data: payload
    :return: response
    """
    response = requests.post(url=url, data=data, json=headers)
    try:
        assert response.status_code == 200 or 201, "expected status code is 200 or 201," \
                                                       " but we got: {}".format(response.status_code)
        return response
    except AssertionError:
        raise ValueError(response.content)
