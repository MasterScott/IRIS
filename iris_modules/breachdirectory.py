import requests, json
from colorama import Fore

apiKey = json.load(open('config.json'))['breachdirectory']

def run(target):
    url = "https://breachdirectory.p.rapidapi.com/"
    querystring = {"func":"auto","term": target}
    headers = {
        'x-rapidapi-key': apiKey,
        'x-rapidapi-host': "breachdirectory.p.rapidapi.com"
    }
    r = requests.request("GET", url, headers=headers, params=querystring).json()
    try:
        for result in r['result']:
            print(f'{Fore.GREEN}•{Fore.RESET} {target}:{result["password"]}')
    except:
        print(f'{Fore.RED}•{Fore.RESET} No Results Found')
