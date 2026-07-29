"""Configuration loader."""

import json
from pathlib import Path

def load_config(path="config.json"):
    config_file = Path(path)
    if config_file.exists():
        return json.loads(config_file.read_text())
    return {"version": "0.1", "debug": False}
