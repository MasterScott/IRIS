import requests, json
from colorama import Fore

def run(target):
    r = requests.post(url=f'https://breachdirectory.com/api_usage?domain=https://test.com&method=ip&query={target}').text.replace('API provided by BreachDirectory.', '')
    r = json.loads(f'[{r.replace("}", "}, ")}]'.replace('\n', '').replace('}, ]', '}]'))
    
    for result in r:
        email = result['email']
        ip = result['ip']
        domain = result['title']
        username = result['username']
        if ip == '': ip = 'None'
        if email == '': email = 'None'
        if domain == '': domain = 'None'
        if username == '': username = 'None'

        print(f'''
Results for {target} using method IP Breach
    {Fore.GREEN}•{Fore.RESET} Email        : {email}
    {Fore.GREEN}•{Fore.RESET} Username     : {username}
    {Fore.GREEN}•{Fore.RESET} IP Address   : {ip}
    {Fore.GREEN}•{Fore.RESET} Domain       : {domain}''')
