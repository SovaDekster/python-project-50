def set_bool_to_low(file):
    for key, value in file.items():
        if type(value) == bool:
            value = str(value).lower()
            file[key] = value
    return file


def set_common_and_difference(file1, file2):
    common = file1.keys() & file2.keys()
    diff_file1 = file1.keys() - file2.keys()
    diff_file2 = file2.keys() - file1.keys()
    return common, diff_file1, diff_file2


if __name__ == '__main__':
    set_bool_to_low(file)  # noqa F821
    set_common_and_difference(file1, file2)  # noqa F821
