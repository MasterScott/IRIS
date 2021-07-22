from colorama import Fore, Back, Style
import os


md = [
        [0, 'Set-Target-<TARGET>', 'Set the target for IRIS.', 'target, set'],
        [1, 'Start-<Module>', 'Search for keybase\'s account email.', 'start, modules, execute'],
        [2, 'Search <KEYWORD>', 'Search for any command based on keywords.', 'search, interactive, keywords'],
        [3, 'Clear', 'Clear all infomation from the screen.', 'clear, cls'],
        [4, 'Help', 'Shows This Help Message.', 'help, modules, infomation']
]

mj = [  
        [1, 'Breach', 'Scan an email for breaches, leaks, and sites the email is active on', 'search, online, email, breach, leak'],
        [2, 'SiteScan', 'Scan various online websites that a user may be signed up on', 'online, email, social, api'],
        [3, 'WeLeakInfo', 'Wrapper for weleakinfo.to to find recent breaches on a targets email', 'online, email, interactive, api'],
        [4, 'Thatsthem', 'Online scan for full name, phone number, and address', 'online, email, interactive, api'],
        [5, 'Twitter', 'Grabs the full email address and phone number of a target account', 'online, email, interactive, api, twitter, leak'],
]


def logo():
    print(f'''{Fore.MAGENTA}
\t\t\t\t    ___     _    
\t\t\t\t   |_ _|_ _(_)___
\t\t\t\t    | || '_| (_-<
\t\t\t\t   |___|_| |_/__/
{Fore.GREEN}
\t\t\t(The Best OSINT Scanner On The Web)                     
''')

def clear():
    os.system('cls')
    logo()

def help():
    clear()
    print(f'''
{Fore.LIGHTBLUE_EX}Interactive :{Fore.RESET}
==========================
    Ctrl+C: Skips Current Scan.
    Ctrl+Z: Stop IRIS.
        
{Fore.LIGHTBLUE_EX}Commands :{Fore.RESET}
==========================''')
    for module in md:
        info_name = module[1].replace("-", " ")
        print(f'    {info_name:<20} : {module[2]}')

    print(f'''
{Fore.LIGHTBLUE_EX}Ledgend Key :{Fore.RESET}
==========================
    {Fore.MAGENTA}•{Fore.RESET} Results
    {Fore.RED}•{Fore.RESET} Error
    {Fore.GREEN}•{Fore.RESET} Success
    {Fore.YELLOW}•{Fore.RESET} Log / Loading
''')

def modules():
    clear()
    print(f'''
{Fore.LIGHTBLUE_EX}Modules :{Fore.RESET}
==========================''')
    for module in mj:
        info_name = module[1].replace("-", " ")
        print(f'    {info_name:<11} : {module[2]}')
    print()