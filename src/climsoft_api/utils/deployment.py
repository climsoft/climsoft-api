import yaml
from pathlib import Path
from typing import Dict, List

deployment_config_file = Path.resolve(Path("./deployment.yml"))


def load_deployment_configs() -> Dict[str, List[Dict[str, str]]]:
    print(deployment_config_file)
    deployment_configs = {}

    if deployment_config_file.exists():
        with open(deployment_config_file, "r") as stream:
            deployment_configs = yaml.safe_load(stream=stream)
    return deployment_configs
