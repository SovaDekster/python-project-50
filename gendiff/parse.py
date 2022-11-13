from pathlib import Path
import yaml
import json


def get_data(path):
    extension = Path(path).suffix[1:]
    if extension == 'json':
        format = 'json'
        data = open(path)
    elif extension == 'yml' or extension == 'yaml':
        format = 'yaml'
        data = open(path)
    return data, format


def parse(data, format: str):
    if format == 'json':
        return json.load(data)
    if format == 'yaml':
        return yaml.safe_load(data)
    else:
        raise Exception(f"No such method for format: {format}")
