import yaml

CONFIG_PATH = "configs/app_config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        config = yaml.load(f)

    return config # return json