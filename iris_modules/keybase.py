import requests, re, base64
from colorama import Fore

def getKeybase(target):
    if '@' in target:
        target = target.split('@')[0]

    endpoint = f'https://keybase.io/_/api/1.0/user/lookup.json?usernames={target}'
    r = requests.get(url=endpoint)
    if r.status_code == 200:
        r = r.json()

        if '@' in target:
            target = target.split('@')[0]

        print(f'{Fore.YELLOW}•{Fore.RESET} Searching for keybase with username : {target}')
        rq = requests.get(f'https://keybase.io/{target}/pgp_keys.asc').text.split('\n\n')
        try:
            key = rq[1].split('-----')
            email = re.findall(r' <.*?>', str(base64.b64decode(key[0])))
            email = email[0].split("<")[1].split(">")[0]
        except:
            email = "None"

        device_ids = []
        used_devices = []
        try:
            user_id = r['them'][0]['id']
            name = r['them'][0]['profile']['full_name']
            location = r['them'][0]['profile']['location']
            bio = r['them'][0]['profile']['bio']
            d = r['them'][0]['devices']

            for device in d:
                device_ids.append(device)
            
            for device in device_ids:
                used_devices.append((r['them'][0]['devices'][device]['name'], r['them'][0]['devices'][device]['type']))

            print(f'{Fore.GREEN}•{Fore.RESET} Scan Complete')
            print(f'''    {Fore.BLUE}•{Fore.RESET} Username       : {target}
    {Fore.BLUE}•{Fore.RESET} Full Name      : {name}
    {Fore.BLUE}•{Fore.RESET} Location       : {location}
    {Fore.BLUE}•{Fore.RESET} Account Bio    : {bio}
    {Fore.BLUE}•{Fore.RESET} Email Address  : {email}
        {Fore.MAGENTA}•{Fore.RESET} Devices''')
            if len(used_devices) > 1:
                print(f'            {Fore.BLUE}•{Fore.RESET} No Devices Found')
            else:
                for device in used_devices:
                    print(f'            {Fore.BLUE}•{Fore.RESET} {device[0]} - {device[1]}')
            print()
        except Exception as e:
            print(f'{Fore.RED}•{Fore.RESET} No Results Found')
    else:
        print(f'{Fore.RED}•{Fore.RESET} No Results Found')
def run(target):
    getKeybase(target)