import subprocess
import random
import os

from iris.logger import Logger

import iris


class ConsoleUtil:
    __BANNER = '''
         \x1b[91m##
       \x1b[91m##\x1b[93m##\x1b[91m##
     \x1b[91m##\x1b[93m##\x1b[94m##\x1b[93m##\x1b[91m##
   \x1b[91m##\x1b[93m##\x1b[94m##\x1b[0m##\x1b[94m##\x1b[93m##\x1b[91m##   \x1b[97mIRIS \x1b[94mv%(version)s \x1b[0mby \x1b[92m%(author)s
   \x1b[91m##\x1b[93m##\x1b[94m##\x1b[0m##\x1b[94m##\x1b[93m##\x1b[91m##   \x1b[90mAn open-source intelligence framework.
     \x1b[91m##\x1b[93m##\x1b[94m##\x1b[93m##\x1b[91m##
       \x1b[91m##\x1b[93m##\x1b[91m##
         \x1b[91m##\x1b[0m
'''
    __BANNER = '''
  \x1b[96m┬  ┬─┐  ┬  ┌─┐  
  \x1b[96m│  ├┬┘  │  └─┐  \x1b[0mrevamped by %(author)s\x1b[0m
  \x1b[96m┴  ┴└─  ┴  └─┘  \x1b[90m@IrisDevTeam
  \x1b[0mv%(version)s        
'''

    @staticmethod
    def clear_screen():
        """ Clear console screen """
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

    @staticmethod
    def set_title(title: str):
        """ Set console title """
        title = title % {'author': iris.__author__, 'version': iris.__version__}
        if os.name == 'nt':
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            print('\x1b]0;' + title, end='\a')

    @staticmethod
    def yn_prompt(prompt: str) -> bool:
        """ Spawn Yes/No prompt """
        while True:
            answer = input(prompt)
            
            if len(answer) == 0:
                continue

            answer = answer.lower()

            if answer.startswith('y'):
                return True

            elif answer.startswith('n'):
                return False

            Logger.warning('Input must be either Yes or No')

    @staticmethod
    def print_banner():
        """ Print banner """
        print(ConsoleUtil.__BANNER.lstrip(' ').replace('##', random.choice('8o.-_#|@0!/\\?+><*`´¨') * 2) % {'version': iris.__version__, 'author': iris.__author__} + '\x1b[0m')
