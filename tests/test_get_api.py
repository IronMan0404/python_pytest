__author__ = 'Bhargava Batchu'

import pytest
import input_data.test_data as test_data
import input_data.api_endpoints.url_data as url_data
from utils.genaral_requests import get_response_from_api
from utils.common import print_errors
from page_objects.get_api_page import get_the_id_value_from_get_api


class TestGetApi:
    @pytest.fixture(scope="module")
    def api_response(self):
        response = get_response_from_api(url_data.BASE_URL + url_data.GET_URI, header=None)
        yield response

    #  Validating the status code
    def test_status_code(self, api_response):
        """
        @param api_response:
        """
        status_code = api_response.status_code
        try:
            assert status_code == test_data.STATUS_CODE_200, "expected status code is 200, " \
                                                             "but we got: {}".format(status_code)
        except AssertionError:
            raise ValueError('Expected Status Code is 200 but we got: {}'.format(status_code))

    def test_response_header(self, api_response):
        """
        @param api_response:
        """
        response_headers = api_response.headers
        failure_headers = list()

        # Get the Content-Type from response headers
        try:
            content_type = response_headers["Content-Type"]
        except KeyError:
            raise ValueError(" Content-Type is not present in response headers")
        try:
            assert content_type == test_data.CONTENT_TYPE
        except AssertionError:
            assertion_error = "Expected content type is {}, but got this: " "{}".format(test_data.CONTENT_TYPE,
                                                                                        content_type)
            failure_headers.append(assertion_error)

        # Get the Content-Encoding from response headers
        try:
            content_encoding = response_headers["Content-Encoding"]
        except KeyError:
            raise ValueError("Content-Encoding is not present in response headers")
        try:
            assert content_encoding == test_data.CONTENT_ENCODING
        except AssertionError:
            assertion_error = ""
            failure_headers.append(assertion_error)

        # Print all failure errors
        assert len(failure_headers) == 0,  'Error are: {}'.format(print_errors(failure_headers))

    def test_id_in_response_content(self, api_response):
        """
        @param api_response:
        """
        id_values = get_the_id_value_from_get_api()
        try:
            assert test_data.EXPECTED_VALUE in id_values, "expected Id not found in my list "
            print(id_values)
        except Exception:
            raise AssertionError("expected Id not found in my list, expected value is 1, "
                                 "and my list is: {}".format(id_values))
