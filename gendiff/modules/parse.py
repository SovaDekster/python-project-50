from pathlib import Path
import yaml
import json


def open_file(path):
    extension = Path(path).suffix
    if extension == '.json':
        format = 'json'
        data = open(path)
    elif extension == '.yml' or extension == '.yaml':
        format = 'yaml'
        data = Path(path).read_text()
    return data, format


def parse(data, format: str):
    if format == 'json':
        return json.load(data)
    if format == 'yaml':
        return yaml.safe_load(data)
