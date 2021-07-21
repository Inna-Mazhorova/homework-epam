import requests
import requests_mock

from homework4.hw4_task02 import count_dots_on_i, read_url_func


def test_url(requests_mock):
    requests_mock.get("http://test.com", text="data_for_test_iiiii")
    site_content = requests.get("http://test.com").text
    assert count_dots_on_i("http://test.com") == 5
