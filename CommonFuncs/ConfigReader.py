import pathlib
from configparser import ConfigParser


def read_test_config(category, key):
    config = ConfigParser()
    curr_file_path = pathlib.Path(__file__).parent.parent.absolute()
    config.read(f"{curr_file_path}/config.ini")
    return config.get(category,key)
