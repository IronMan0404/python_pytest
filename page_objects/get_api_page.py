import json
import input_data.api_endpoints.url_data as url_data
from utils.genaral_requests import get_response_from_api


def get_the_id_value_from_get_api():
    """
    this function returns the only list of Id values from API response
    :return: response
    :return: list of id values
    """
    id_list = list()
    response = get_response_from_api(url_data.BASE_URL+ url_data.GET_URI, header=None)
    data = json.loads(response.content)
    data_length = len(data["data"])
    for i in range(data_length):
        id_list.append(data["data"][i]["id"])
    return id_list
