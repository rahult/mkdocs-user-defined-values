import pytest
from plugin.plugin import UserDefinedValues


@pytest.fixture()
def plugin():
    """ Helper to initiate UserDefinedValues object"""
    return UserDefinedValues()


def test_plugin_default_config(plugin):
    expected = {"keywords": None, "input-placeholder": "{{{user-defined-values}}}"}
    errors, warnings = plugin.load_config({})
    assert plugin.config == expected
    assert errors == []
    assert warnings == []


def test_plugin_config_input_placeholder(plugin):
    expected = {"keywords": None, "input-placeholder": "{{{custom-placeholder}}}"}
    errors, warnings = plugin.load_config(
        {"input-placeholder": "{{{custom-placeholder}}}"}
    )
    assert plugin.config == expected
    assert errors == []
    assert warnings == []


def test_plugin_config_keywords(plugin):
    expected = {
        "keywords": {"YOUR_AWS_REGION": {"placeholder": "e.g. ap-southeast-2"}},
        "input-placeholder": "{{{user-defined-values}}}",
    }
    errors, warnings = plugin.load_config(
        {"keywords": {"YOUR_AWS_REGION": {"placeholder": "e.g. ap-southeast-2"}}}
    )
    assert plugin.config == expected
    assert errors == []
    assert warnings == []


def test_plugin_on_config_sanitize_all_keywords_to_be_dict(plugin, load_config):
    expected = {"YOUR_AWS_REGION": {}}
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config(
        {"keywords": {"YOUR_AWS_REGION": "placeholder"}}
    )
    plugin.on_config(load_config)
    assert plugin.keywords == expected
    assert errors == []
    assert warnings == []
