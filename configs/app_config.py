""" Configuration class to load environment variables from .env file
    and handle any other configuration related tasks.
    (add more methods as needed)
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


class AppConfig:
    PROJECT_ROOT = Path(__file__).parents[1]
    MODEL_PATH = PROJECT_ROOT / "models"
    STATIC_PATH = PROJECT_ROOT / "api/static"
    __instance = None

    @staticmethod
    def get_config_instance():
        if AppConfig.__instance is None:
            AppConfig.__instance = AppConfig()
        return AppConfig.__instance

    def __init__(self):
        if AppConfig.__instance is not None:
            raise Exception("This is a singleton class and can't be instantiated more than once.")
        self._load_configs()

    def _load_configs(self):
        self.configs = dict(os.environ)

    def get(self, key, default=None) -> Optional["str"]:
        return self.configs.get(key, default)

    def set(self, key: str, value):
        self.configs[key] = value


if __name__ == "__main__":
    app_config = AppConfig.get_config_instance()
    print(app_config.STATIC_PATH)
