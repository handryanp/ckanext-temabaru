"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.temabaru.logic import validators


def test_temabaru_reauired_with_valid_value():
    assert validators.temabaru_required("value") == "value"


def test_temabaru_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.temabaru_required(None)
