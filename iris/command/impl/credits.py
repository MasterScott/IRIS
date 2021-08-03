from iris.command import Command

import iris


class CreditsCommand(Command):
    name = 'credits'
    description = 'Show IRIS OSINT Framework credits'
    aliases = ['credit']
    
    @Command.execute
    def run(self):
        print(rf'''
 ___ ____  ___ ____  
|_ _|  _ \|_ _/ ___| 
 | || |_) || |\___ \ 
 | ||  _ < | | ___) |
|___|_| \_\___|____/ 
                      

IRIS version {iris.__version__}: an open-source intelligence framework 

Developed by {iris.__author__}

GitHub:
    https://github.com/IRIS-Team/IRIS-Framework.git

Twitter:
    https://www.twitter.com/elordcs
    https://www.twitter.com/infectedbrowser''')
