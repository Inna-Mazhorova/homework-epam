import urllib.request
from unittest.mock import patch

from homework4.hw4_task02 import count_dots_on_i


def test_url():
    class FakeResponse:
        def __init__(self, url, content):
            self.url = url
            self.content = content

    def fake_get(*args, **kwargs):
        return FakeResponse(url="https://for_test/", content=b"data_for_test_iiiii")

    with patch("urllib.request.urlopen", new=fake_get):
        assert count_dots_on_i("https://example.com/for_test") == 5
