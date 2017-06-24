import os
import json
import glob
import shutil

# -----------------------------------
# Path/Dirs

CFG_PATH = "mud-utils.cfg"
IMAGES_DIR = "/images"
TMP_DIR = "/tmp/mud-utils"
TMP_PACKAGE_CONFIGS = "/tmp/mud-utils/config.lua"
PROJ_CONFIGS = "config.lua"

# -----------------------------------
# Config Vars

VAR_PROJ_PATH = "proj_path"
VAR_PACKAGE_PATH = "package_path"

# -----------------------------------
# Core methods


def configure(cfg_path):
    global configs
    with open(cfg_path) as cfgs:
        configs = json.load(cfgs)


configure(CFG_PATH)

# -----------------------------------
# Access configs


def proj_path():
    return configs[VAR_PROJ_PATH]


def package_path():
    return configs[VAR_PACKAGE_PATH]

def tmp_package_configs():
    return TMP_PACKAGE_CONFIGS


def proj_configs():
    return configs[VAR_PROJ_PATH] + '/' + PROJ_CONFIGS


def images_path():
    return configs[VAR_PROJ_PATH] + IMAGES_DIR


def tmp_path():
    return TMP_DIR


# -----------------------------------
# Dir functions


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def delete_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

# -----------------------------------
# Files functions


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def write_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)


def write_json(path, dict_data):
    write_file(path, json.dumps(dict_data, indent=4))


def find_files(pattern_file):
    return glob.glob(pattern_file)


def copy_file(src_path, dst_path):
    shutil.copyfile(src_path, dst_path)


def get_file_from_path(path):
    return path.split("/")[-1]


# -----------------------------------
# Configs validation
try:
    os.path.exists(proj_path())
except BaseException:
    raise NotADirectoryError(
        "{} 'proj_path' configuration isn't a valid directory.\nTry to configure a full path.".format(
            configs[VAR_PROJ_PATH]))
# -----------------------------------
