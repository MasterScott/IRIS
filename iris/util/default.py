import os


class DefaultUtil:

    OUT_PATH: str = os.path.join(os.getenv('APPDATA' if os.name == 'nt' else 'HOME'), '.iris1', 'local')    
    """ Default output file path """