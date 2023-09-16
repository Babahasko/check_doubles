import os
from dataclasses import dataclass
from pathlib import Path
import hashlib
from collections import Counter



@dataclass(frozen=True)
class FileInfo:
    file_name: str
    file_path: str
    size: float
    sha1: str


class Directory:

    def __init__(self):
        self._dirinfo = set([])

    def __repr__(self):
        return f"Directory {self._dirinfo}"

    # def __eq__(self, other):
    #     if not isinstance(other, Directory):
    #         return False
    #     return other._dirinfo == self._dirinfo
    #
    # def __hash__(self):
    #     return hash(self._dirinfo)

    def add(self, line: FileInfo):
        self._dirinfo.add(line)


def read_paths(dst_path):
    """
    Эта функция производит обход каталога и
    записывает экземпляры классов FileInfo
    :param dst_path:
    :return:
    """
    directory_info = Directory()
    for folder, _, files in os.walk(dst_path):
        for fn in files:
            size = file_size(Path(folder) / fn)
            sha1 = hash_file(Path(folder) / fn)
            line = FileInfo(file_name=fn, file_path=folder, size=size, sha1=sha1)
            directory_info.add(line)
    return directory_info

def file_size(file_path):
    """
    This function will return file size
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

block = 65536

def hash_file(path):
    hash_function = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(block)
        while buf:
            hash_function.update(buf)
            buf = file.read(block)
    return hash_function.hexdigest()

def check_doubles(dir_info):
    all_sha = []
    for file_info in dir_info._dirinfo:
        sha = file_info.sha1
        all_sha.append(sha)
    if len(set(all_sha)) == len(all_sha):
        pass
    else:
        Counter(all_sha)
        dublicates = [key for key in Counter(all_sha) if Counter(all_sha)[key] > 1]
        print('dublicates = ', dublicates)
        for item in dir_info._dirinfo:
            if item.sha1 in dublicates:
                path_to_dublicate = Path(item.file_path) / item.file_name
                os.remove(path_to_dublicate)
                print('Удален файл', path_to_dublicate)



def check_sha(dir_info):
    all_sha = []
    for file_info in dir_info._dirinfo:
        sha = file_info.sha1
        all_sha.append(sha)
    if len(set(all_sha)) == len(all_sha):
        print('len set = ', len(set(all_sha)), 'len list', len(all_sha))
        return True
    else:
        print('len set = ', len(set(all_sha)), 'len list', len(all_sha))
        return False



if __name__ == "__main__":
    dir_name = 'test_directory'
    path_to_dir = Path(os.getcwd()) / dir_name
    dir_info = read_paths(path_to_dir)
    print(dir_info)
