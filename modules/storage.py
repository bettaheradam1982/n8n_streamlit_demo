import json
import os

CONFIG_PATH = "data/config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {"max_backups": 7, "summary_language": "DE"}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    os.makedirs("data", exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
