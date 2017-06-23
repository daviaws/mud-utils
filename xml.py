import configs

PATTERN = "/*.xml"


def find_files(path):
    pattern = path + PATTERN
    return configs.find_files(pattern)


def to_triggers_proj(path, triggers_path):
    print(path)
