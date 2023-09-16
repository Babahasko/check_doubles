import tempfile
from pathlib import Path
import os
import random
import shutil
import string

def make_content():
    text_length = random.randint(1, 50)
    random_text = []
    for i in range(text_length):
        random_letter = random.choice(string.ascii_letters)
        random_text.append(random_letter)
    return "".join(random_text)



def make_test_dir(dir_name):
    path_to_dir = Path(os.getcwd()) / dir_name
    try:
        Path(path_to_dir).mkdir()
    except FileExistsError:
        print("Директория уже существует")
    return path_to_dir


def make_random_files(test_dir_path):
    os.chdir(test_dir_path)
    i = 0
    for num in range(20):
        # let the file begin with a random number between 1 to 50
        file_name = make_content()
        Path(file_name).touch()
        content = make_content()
        Path(file_name).write_text(content)
        if i == 5:
            file_name = make_content()
            Path(file_name).write_text(content)
        i += 1
    os.chdir('..')

def remove_test_dir(test_dir_path):
    shutil.rmtree(test_dir_path)


if __name__ == "__main__":

    path_to_dir = make_test_dir('test_directory')
    #make_random_files(path_to_dir)
    shutil.rmtree(path_to_dir)


