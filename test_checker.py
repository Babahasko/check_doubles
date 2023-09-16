import tempo
import shutil
from checker import check_doubles, check_sha, read_paths

directory = 'test_directory'


def make_test_directory(directory):
    path_to_dir = tempo.make_test_dir(directory)
    tempo.make_random_files(path_to_dir)
    return path_to_dir


def remove_test_directory():
    shutil.rmtree(directory)


def test_all_files_are_different():
    try:
        dst_path = make_test_directory(directory)
        dir_info = read_paths(dst_path)
        check_doubles(dir_info)
        new_dir = read_paths(dst_path)
        assert check_sha(new_dir) == True

    finally:
        remove_test_directory()

# def test_parse_dir_path:
#     try:
