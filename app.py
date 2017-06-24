import configs
import images
import package

import time


# API - Just use this functions
def correct_pngs(path):
    png_files = images.find_png_files(path)
    for png_file in png_files:
        images.call_corretion_script(png_file)


def convert_package_to_proj():
    package.create_proj_tree()
    configs.create_dir(configs.tmp_path())
    package.exctract_package(configs.package_path(), configs.tmp_path())
    package.move_pngs(configs.tmp_path(), configs.proj_path())
    package.move_configs(configs.tmp_package_configs(), configs.proj_configs())
    package.convert_xml_to_proj(configs.tmp_path(), configs.proj_path())
    time.sleep(1)
    configs.delete_dir(configs.tmp_path())


def convert_proj_to_package():
    pass

convert_package_to_proj()
