import os


def create_directory_if_doesnt_exists(directory):
    if not directory_exists(directory):
        os.makedirs(directory)


def directory_exists(directory):
    return os.path.exists(directory)
