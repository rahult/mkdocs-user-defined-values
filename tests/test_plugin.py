import pytest
from plugin.plugin import *


def test_plugin_default_config():
    expected = {"keywords": None, "input-placeholder": "{{{user-defined-values}}}"}
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config({})
    assert plugin.config == expected
    assert errors == []
    assert warnings == []


def test_plugin_config_input_placeholder():
    expected = {"keywords": None, "input-placeholder": "{{{custom-placeholder}}}"}
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config(
        {"input-placeholder": "{{{custom-placeholder}}}"}
    )
    assert plugin.config == expected
    assert errors == []
    assert warnings == []


def test_plugin_config_keywords():
    expected = {
        "keywords": {"YOUR_AWS_REGION": {"placeholder": "e.g. ap-southeast-2"}},
        "input-placeholder": "{{{user-defined-values}}}",
    }
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config(
        {"keywords": {"YOUR_AWS_REGION": {"placeholder": "e.g. ap-southeast-2"}}}
    )
    assert plugin.config == expected
    assert errors == []
    assert warnings == []
