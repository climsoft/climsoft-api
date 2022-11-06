import copy

import yaml
from pathlib import Path
from typing import Dict
from pydantic import BaseSettings
from climsoft_api.config import settings, Settings

deployment_config_file = Path.resolve(Path("./deployment.yml"))


def load_deployment_configs() -> Dict[str, Dict[str, str]]:
    deployment_configs = {}

    if deployment_config_file.exists():
        with open(deployment_config_file, "r") as stream:
            deployment_configs = yaml.safe_load(stream=stream)
    return deployment_configs


def override_settings(overrides: Dict[str, str]) -> Settings:
    if overrides.get("NAME"):
        overrides.pop("NAME")
    settings_copy = copy.deepcopy(settings)
    for k, v in overrides.items():
        setattr(settings_copy, k, v)
    return settings_copy
