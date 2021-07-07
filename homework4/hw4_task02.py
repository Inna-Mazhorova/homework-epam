import urllib.request

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


def count_dots_on_i(url):
    try:
        r = urllib.request.urlopen(url)
        site_content = r.read()
        encoding = r.info().get_content_charset()
        site_content_html = site_content.decode(encoding)

        counter = 0
        for symbol in site_content_html:
            if symbol == "i":
                counter += 1
        return counter
    except Exception:
        return "Unreachable url"
