import requests
import requests_mock

from homework4.hw4_task02 import count_dots_on_i


def test_url(requests_mock):
    requests_mock.get("http://test.com", text="data_for_test_iiiii")
    site_content = requests.get("http://test.com").text
    counter = 0
    for symbol in site_content:
        if symbol == "i":
            counter += 1
    return counter
    assert counter == 5
