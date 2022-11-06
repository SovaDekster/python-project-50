from pathlib import Path
import json
import yaml


def open_file(path):
    format = Path(path).suffix
    if format == '.json':
        return json.load(open(path))
    if format == '.yml' or format == '.yaml':
        return yaml.safe_load(Path(path).read_text())


if __name__ == '__main__':
    open_file(path)  # noqa: F821
