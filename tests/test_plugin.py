import pytest
from plugin.plugin import UserDefinedValues
import os
from mkdocs import config


def load_config(**cfg):
    """ Helper to build a simple config for testing. """
    path_base = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "demo")
    cfg = cfg or {}
    if "site_name" not in cfg:
        cfg["site_name"] = "Example"
    if "config_file_path" not in cfg:
        cfg["config_file_path"] = os.path.join(path_base, "mkdocs.yml")
    if "docs_dir" not in cfg:
        # Point to an actual dir to avoid a 'does not exist' error on validation.
        cfg["docs_dir"] = os.path.join(path_base, "docs")
    conf = config.Config(
        schema=config.DEFAULT_SCHEMA, config_file_path=cfg["config_file_path"]
    )
    conf.load_dict(cfg)

    errors_warnings = conf.validate()
    assert errors_warnings == ([], []), errors_warnings
    return conf


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


def test_plugin_on_config_sanitize_all_keywords_to_be_dict(plugin):
    expected = {"YOUR_AWS_REGION": {}}
    plugin = UserDefinedValues()
    errors, warnings = plugin.load_config(
        {"keywords": {"YOUR_AWS_REGION": "placeholder"}}
    )
    plugin.on_config(load_config(theme="mkdocs", extra_javascript=[]))
    print(plugin.keywords)
    assert plugin.keywords == expected
    assert errors == []
    assert warnings == []
