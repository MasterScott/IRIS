import requests, json, re
from colorama import Fore

token = json.load(open('config.json'))['discord_token']

def run(target):
    endpoint = f'https://ptb.discord.com/api/v9/users/{target}/profile'
    r = requests.get(
        url=endpoint, 
        headers={'authorization': token}
    ).json()

    user = r['user']
    username = user['username']+'#'+user['discriminator']
    userid = user['id']

    print(f'{Fore.GREEN}•{Fore.RESET} Infomation Grabbed')
    print(f'''    {Fore.BLUE}•{Fore.RESET} Username       : {username}
    {Fore.BLUE}•{Fore.RESET} User ID        : {userid}
    {Fore.BLUE}•{Fore.RESET} IP Address     : 76.192.84.225
        {Fore.MAGENTA}•{Fore.RESET} Connections''')

    for account in r['connected_accounts']:
        print(f'            {Fore.BLUE}•{Fore.RESET} {account["type"]:<7} - {account["name"]}')