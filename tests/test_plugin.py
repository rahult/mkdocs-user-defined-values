import pytest
from plugin.plugin import *


@pytest.mark.parametrize(
    "key,expected",
    [("keywords", None), ("input-placeholder", "{{{user-defined-values}}}")],
)
def test_plugin_default_config(key, expected):
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config({})
    assert plugin.config[key] == expected
    assert errors == []
    assert warnings == []


def test_plugin_config_input_placeholder():
    expected = {"keywords": None, "input-placeholder": "{{{custom-placehoder}}}"}
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config(
        {"input-placeholder": "{{{custom-placeholder}}}"}
    )
    assert sorted(plugin.config) == sorted(expected)
    assert errors == []
    assert warnings == []
