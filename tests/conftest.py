import pytest
import os
from mkdocs import config


@pytest.fixture()
def load_config():
    """ Helper to build a simple config for testing. """
    # Point to an actual dir to avoid a 'does not exist' error on validation.
    path_base = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "demo")
    cfg = {}
    cfg["site_name"] = "Example"
    cfg["config_file_path"] = os.path.join(path_base, "mkdocs.yml")
    cfg["docs_dir"] = os.path.join(path_base, "docs")
    conf = config.Config(
        schema=config.DEFAULT_SCHEMA, config_file_path=cfg["config_file_path"]
    )
    conf.load_dict(cfg)

    errors_warnings = conf.validate()
    assert errors_warnings == ([], []), errors_warnings
    return conf
