# Use this module correct_pngs function if you're having "iCCP: known
# incorrect sRGB profile" warning

import configs

import subprocess
import os

PATTERN_PNG = "/*.png"


def find_png_files(path):
    pattern = path + PATTERN_PNG
    return configs.find_files(pattern)


def call_corretion_script(file_path):
    script_path = os.getcwd() + "/correct_png.sh"
    subprocess.check_call([script_path, file_path])


def correct_pngs():
    for file_path in find_png_files(configs.proj_path()):
        if file_path is not None:
            call_corretion_script(file_path)


correct_pngs()
