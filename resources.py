from pathlib import Path


def resource_path(file_name):
    return Path(__file__).parent.joinpath(f"{file_name}").absolute()
