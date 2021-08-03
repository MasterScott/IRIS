import os


class DefaultUtil:

    OUT_PATH: str = os.path.join(os.getenv('HOME'), '.iris1', 'local')
    """ Default output file path """
