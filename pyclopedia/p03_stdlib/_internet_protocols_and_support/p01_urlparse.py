#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
urlparse是一个用于对url进行操作的库。
"""

import six

if six.PY2:
    import urlparse
elif six.PY3:
    import urllib.parse as urlparse


def test_urlsplit():
    """

    **中文文档**

    将url的各个成分分离。
    """
    url = "https://docs.python.org/3/library/urllib.parse.html"
    result = urlparse.urlsplit(url)
    assert result.scheme == "https"
    assert result.netloc == "docs.python.org"
    assert result.path == "/3/library/urllib.parse.html"

    url = "https://docs.python.org/3/search.html?q=urlparse&check_keywords=yes&area=default"
    assert urlparse.urlsplit(
        url).query == "q=urlparse&check_keywords=yes&area=default"


test_urlsplit()


def test_urljoin():
    """

    **中文文档**

    urlparse.urljoin是将第一个url的domain(第3个/以后的内容全部不要), 与剩下
    的parts连接起来。
    """
    url = "https://docs.python.org/3/library/urllib.parse.html"
    assert urlparse.urljoin(
        "https://docs.python.org/", "/3/library/urllib.parse.html") == url

    url = "https://www.example.com/a.html"
    assert urlparse.urljoin(
        "https://www.example.com/a/b/c/", "/a.html") == url

    url = "https://www.example.com/a/b/c.html"
    assert urlparse.urljoin(
        "https://www.example.com/", "a/b" "/c.html") == url


test_urljoin()
