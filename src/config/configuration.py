import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_DIR = os.path.dirname(__file__)
SETTING_FILE = "settings.yaml"
CONFIG_YAML = CONFIG_DIR.replace("/", "\\") + "\\" + SETTING_FILE
