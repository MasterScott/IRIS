import os
from colorama import Fore
from iris_modules import helpers, thatsthem, sitescan, keybase, weleakinfo, twitterleak, helpp, breachdirectory, instagram, emailguess, minecraft, discord, breachdic, ipleak

def logo():
    print(f'''{Fore.MAGENTA}
\t   ___     _    
\t  |_ _|_ _(_)___
\t   | || '_| (_-<  Creator: {Fore.RED}HellSec{Fore.MAGENTA}
\t  |___|_| |_/__/  Version: {Fore.RED}Developer v3.1.4
{Fore.RESET}
[1] Keybase
[2] WeLeakInfo
[3] Twitter
[4] Site Scan
[5] Breach
[6] Instagram
[7] Email Breach
[8] IP Breach

[x] Mass WeLeakInfo
''')

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    logo()

def startCommand():
    clear()
    target = 'None'
    file = 'None'
    while True:
        command = input(f'{Fore.MAGENTA}•{Fore.RESET} IRIS(target={target}, file={file}) ~# ')

        if 'set target' in command.lower():
            target = command.split('target')[1].replace(' ', '')
            if target == 'None' or target == '':
                print(f'{Fore.RED}•{Fore.RESET} To start a module please')
                return
        if 'set file' in command.lower():
            file = command.split('file')[1].replace(' ', '')

        if command.lower() == 'help':
            helpp.help()

        if command.lower() == 'modules':
            helpp.modules()

        if 'clear' in command.lower():
            clear()

        if 'exit' == command.lower():
            exit('Goodbye')

        if 'start' in command.lower():
            try:
                module = command.split('start ')[1].replace(' ', '').lower()

                if module.lower() == '1':
                    keybase.run(target)
                if module.lower() == '2' or module.lower() == 'wli':
                    weleakinfo.run(target, False)
                if module.lower() == 'x':
                    for target in open(file, 'r').readlines():
                        target = target.rstrip()
                        weleakinfo.run(target, True)
                        print()
                if module.lower() == '3':
                    twitterleak.run(target)
                if module.lower() == '4':
                    sitescan.run(target)
                if module.lower() == '5':
                    breachdirectory.run(target)
                if module.lower() == '6':
                    instagram.run(target)
                if module.lower() == '7':
                    breachdic.run(target)
                if module.lower() == '8':
                    ipleak.run(target)
                if module.lower() == 'discord':
                    discord.run(target)
                if module.lower() == 'guess' or module.lower() == 'brute':
                    emailguess.run(target)

            except Exception as e:
                print(e)
