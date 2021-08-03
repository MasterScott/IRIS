import os, threading
from colorama import Fore
from iris_modules import helpers, thatsthem, sitescan, keybase, weleakinfo, twitterleak, helpp, breachdirectory, instagram, emailguess, minecraft, discord, breachdic, ipleak

def logo():
    print(f'''{Fore.MAGENTA}
   ___     _    
  |_ _|_ _(_)___
   | || '_| (_-<  Creator: {Fore.RED}HellSec{Fore.MAGENTA}
  |___|_| |_/__/  Version: {Fore.RED}Public v0.0.9
{Fore.RESET}
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
        command = input(f'{Fore.MAGENTA}•{Fore.RESET} IRIS(target={Fore.RED}{target}{Fore.RESET}, file={Fore.RED}{file}{Fore.RESET}) > ')

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

                if module.lower() == 'keybase':
                    keybase.run(target)
                if module.lower() == 'weleakinfo' or module.lower() == 'wli':
                    weleakinfo.run(target, False, True, False)

                if module.lower() == 'masswli' or module.lower() == 'x':
                    count = 0
                    threads = []

                    if file == '':
                        file = 'targets.txt'

                    a = open(file, 'r').readlines()
                    
                    for target in a:
                        target = target.rstrip()
                        t = threading.Thread(target=weleakinfo.run, args=(target, True, False, False))
                        threads.append(t)

                    for x in threads:
                        count += 1
                        clear()
                        print(f'{Fore.YELLOW}•{Fore.RESET} Started {count}/{len(a)} Threads')
                        x.start()

                    for x in threads:
                        x.join()

                    print(f'{Fore.GREEN}•{Fore.RESET} Finished Scanning {count}/{len(a)} Targets')

                if module.lower() == 'twitter':
                    twitterleak.run(target)
                if module.lower() == 'sitescan':
                    sitescan.run(target)
                if module.lower() == 'bd':
                    breachdirectory.run(target)
                if module.lower() == 'ig':
                    instagram.run(target)
                if module.lower() == 'breach':
                    breachdic.run(target)
                if module.lower() == 'ip':
                    ipleak.run(target)
                if module.lower() == 'discord':
                    count = 0
                    connections = discord.run(target)
                    print()
                    for target in connections:
                        count += 1
                        name = target['name']
                        name = name.rstrip()
                        typ = target['type']
                        print(f'{Fore.MAGENTA}•{Fore.RESET} Searching for {name} on {typ}')
                        weleakinfo.run(name, False, True, False)

                    print(f'{Fore.GREEN}•{Fore.RESET} Finished Scanning {count}/{len(connections)} Targets')

                    target = None

                if module.lower() == 'guess' or module.lower() == 'brute':
                    emailguess.run(target)

            except Exception as e:
                print(e)
