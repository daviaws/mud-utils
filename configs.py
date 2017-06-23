import os
import json
import glob
import shutil

# -----------------------------------
# Path/Dirs

CFG_PATH = "mud-utils.cfg"
IMAGES_DIR = "/images"
TRIGGERS_DIR = "/triggers"
TMP_DIR = "/tmp/mud-utils"

# -----------------------------------
# Config Vars

VAR_PROJ_PATH = "proj_path"

TRIGGERS = "Triggers"

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


def images_path():
    return configs[VAR_PROJ_PATH] + IMAGES_DIR


def triggers_path():
    return configs[VAR_PROJ_PATH] + TRIGGERS_DIR


def tmp_path():
    return TMP_DIR


def triggers():
    return TRIGGERS

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
