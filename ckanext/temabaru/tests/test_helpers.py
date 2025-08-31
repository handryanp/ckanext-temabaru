"""Tests for helpers.py."""

import ckanext.temabaru.helpers as helpers


def test_temabaru_hello():
    assert helpers.temabaru_hello() == "Hello, temabaru!"
