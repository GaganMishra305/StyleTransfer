import json
import os
from functools import lru_cache
from typing import Dict, Any

class Config:
    @staticmethod
    @lru_cache(maxsize=1)
    def load_config() -> Dict[str, Any]:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading config: {str(e)}")

    @classmethod
    def get_model_config(cls, model_type: str) -> Dict[str, Any]:
        return cls.load_config().get(f'{model_type}_model', {})