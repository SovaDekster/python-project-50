from pathlib import Path
import yaml
import json


def parse(data, format: str):
    if format == 'json':
        return json.load(data)
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(data)
    raise Exception(f"No such method for format: {format}")


def get_content_and_extension(path):
    format = Path(path).suffix[1:]
    data = open(path)
    return data, format
