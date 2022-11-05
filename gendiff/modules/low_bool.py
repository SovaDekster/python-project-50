def get_bool_to_low(file):
    for key, value in file.items():
        if type(value) == bool:
            value = str(value).lower()
            file[key] = value
    return file


if __name__ == '__main__':
    get_bool_to_low(file)  # noqa F821
