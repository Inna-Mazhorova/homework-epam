import requests

"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
"""


def read_url_func(url):
    try:
        with requests.get(url) as r:
            site_content = r.text
    except urllib.error.URLError:
        raise ValueError("Unreachable", {url})
    return site_content


def count_dots_on_i(url):
    site_content = read_url_func(url)
    try:
        counter = site_content.count("i")
        return counter
    except Exception:
        return "Problems with counting"


print(count_dots_on_i("https://example.com/"))
