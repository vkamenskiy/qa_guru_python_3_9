import os

import resources


def abs_path(file: str):
    return os.path.abspath(os.path.join(os.path.dirname(resources.__file__), file))
