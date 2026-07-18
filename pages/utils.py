from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / 'data' / 'infographics.json'

with open(JSON_FILE, encoding='utf-8') as f:
    infographs = json.load(f)