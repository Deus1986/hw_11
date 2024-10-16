from pathlib import Path

import HW9


def resource_path(file_name):
    return Path(HW9.__file__).parent.joinpath(f"{file_name}").absolute()
