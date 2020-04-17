import pytest
import input_data.test_data as test_data
import input_data.api_endpoints.url_data as url_data
from utils.genaral_requests import get_response_from_api
from page_objects.get_api_page import get_the_id_value_from_get_api


class TestGetApi:
    @pytest.fixture(scope="module")
    def api_response(self):
        response = get_response_from_api(url_data.BASE_URL + url_data.GET_URI, header=None)
        yield response

    def test_status_code(self, api_response):
        status_code = api_response.status_code
        try:
            assert status_code == test_data.STATUS_CODE_200, "expected status code is 200, " \
                                                             "but we got: {}".format(status_code)

        except AssertionError:
            raise ValueError('Expected Status Code is 200 but we got: {}'.format(status_code))


    def test_response_header(self, api_response):
        response_headers = api_response.headers
        print(response_headers["Content-Type"])
        print(response_headers["Content-Encoding"])
        print(response_headers)


    def test_response_content(self, api_response):
        response = api_response.content
        print(response)


        # id_values = get_the_id_value_from_get_api()
        # print(id_values)
        # response = api_response.content
        # print(response)

        # try:
        #     assert test_data.EXPECTED_VALUE in id_values, "expected Id not found in my list "
        #     print(id_values)
        # except Exception:
        #     raise AssertionError("expected Id not found in my list, expected value is 1, "
        #                          "and my list is: {}".format(id_values))
