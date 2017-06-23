import configs
import xml
import images

import os
from zipfile import ZipFile

package_name = "Zulah_D3_GUI.mpackage"
package_path = os.getcwd() + "/" + package_name


def exctract_package(src_dir):
    with ZipFile(src_dir, 'r') as zfile:
        zfile.extractall(configs.TMP_DIR)


def move_pngs_to_proj():
    png_files = images.find_png_files(configs.tmp_path())
    for png_file in png_files:
        dst_file = configs.images_path() + "/" + configs.get_file_from_path(png_file)
        configs.copy_file(png_file, dst_file)


def create_proj_tree():
    configs.create_dir(configs.proj_path())
    configs.create_dir(configs.images_path())
    configs.create_dir(configs.triggers_path())


def convert_xml_to_proj():
    xml_files = xml.find_files(configs.tmp_path())
    for xml_file in xml_files:
        if configs.triggers() in xml_file:
            xml.to_triggers_proj(xml_file, configs.triggers_path())


def convert_package_to_proj(package_path):
    create_proj_tree()
    configs.create_dir(configs.TMP_DIR)
    exctract_package(package_path)
    move_pngs_to_proj()
    # convert_xml_to_proj()
    # configs.delete_dir(configs.TMP_DIR)


convert_package_to_proj(package_path)
