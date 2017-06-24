import configs
import xml_utils
import images

from zipfile import ZipFile


def exctract_package(src_path, dst_path):
    with ZipFile(src_path, 'r') as zfile:
        zfile.extractall(dst_path)


def move_pngs(src_path, dst_path):
    png_files = images.find_png_files(src_path)
    for png_file in png_files:
        dst_file = configs.images_path() + "/" + configs.get_file_from_path(png_file)
        configs.copy_file(png_file, dst_file)


def move_configs(src_path, dst_path):
    configs.copy_file(src_path, dst_path)


def create_proj_tree():
    configs.create_dir(configs.proj_path())
    configs.create_dir(configs.images_path())


def create_package_path():
    configs.create_dir(configs.package_path())


def convert_xml_to_proj(src_path, dst_path):
    xml_files = xml_utils.find_files(src_path)
    for xml_file in xml_files:
        xml_utils.to_proj(xml_file, dst_path)
