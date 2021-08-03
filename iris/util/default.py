import os


class DefaultUtil:
    if os.name == 'nt':
        path = 'appdata'
    else:
        path = 'home'
    
    OUT_PATH: str = os.path.join(os.getenv(path), '.iris1', 'local')    
    """ Default output file path """
