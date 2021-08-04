import os, time

class DefaultUtil:
    if os.name == 'nt':
        path = 'appdata'
    else:
        path = 'home'
    
    print(f'Using {path} as temp Dir')
    try:
        OUT_PATH: str = os.path.join(os.getenv(path), '.iris1', 'local')    
        """ Default output file path """
    except Exception as e:
        print(f'Could not open default temp patch, skipping path.')
        time.sleep(5)