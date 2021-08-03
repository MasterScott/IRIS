import requests, json
from prettytable import PrettyTable 
from colorama import Fore

apiKey = json.load(open('config.json'))['weleakinfo_key']

def wli(option, target):
    results = []
    try:
        r = requests.get(f'https://api.weleakinfo.to/api?value={target}&type={option}&key={apiKey}').json()
    except:
        pass
    try:
        for info in r['result']:
            sources = info["sources"]
            if len(sources) > 0:
                sources = ', '.join(sources)
            else:
                sources = 'Unknown Source'

            if info["line"].split(':')[1] == '' or info["line"].split(':')[1] == ' ':
                pass
            else:
                results.append(f'{info["line"]} - {sources}')
    except:
        results.append('No Results Found')
    return results

def main(target, saveoutput, output):
    results = wli('email', target)
    for result in results:
        if saveoutput == True and 'No Results Found' not in result:
            f = open('results.txt', 'a')
            f.write(f'{result}\n')
            f.close()

    if output == True:
        if 'no results' in result.lower():
            print(f'    {Fore.RED}•{Fore.RESET} {result}')
        else:
            print(f'    {Fore.GREEN}•{Fore.RESET} {result}')

def run(target, saveoutput, output, a):
    if a == True:
        print(f'{Fore.YELLOW}•{Fore.RESET} Searching for leaks with email : {target}')
    try: main(target, saveoutput, output)
    except Exception as e: print(e); return False