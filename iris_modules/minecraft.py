import requests, json
from colorama import Fore

HEADERS = {"PHPSESSID": "jh7v0e3dfoocumo63fd0gnqs0u", "__cfduid": "__cfduid", "cf_clearance": "f0e48275867e8734ff73452743e295338732473a-1624550475-0-150"} # cf cookies

def get_account_uuid(target:str):
    try:
        uuid_response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{target}").json()
        return uuid_response['id']

    except:
        return "uuid_error"

def get_past_usernames(targetuuid:str):
    USERNAMES = []

    pas_user_response = requests.get(f'https://api.mojang.com/user/profiles/{targetuuid}/names')

    for x in range(len(pas_user_response.json())):
        USERNAMES.append(pas_user_response.json()[x]['name'])
    return USERNAMES

def get_migrated(targetuuid:str):
    try:
        r = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{targetuuid}')

        if r.status_code == 200:
            return True
        else:
            return False

    except:
        return False

def optifine_cape(targetuuid:str):
    r = requests.get(f'http://s.optifine.net/capes/{targetuuid}.png')

    if int(r.status_code) == 200:
        return True
    else:
        return False

def run(target: str):
    if '@' in target:
        target = target.split('@')[0]
        
    main_target_uuid = get_account_uuid(target)

    if main_target_uuid != None or "uuid_error":
        print(f'{Fore.GREEN}•{Fore.RESET} Infomation Found')
        main_target_past_usernames = get_past_usernames(main_target_uuid)
        main_target_migrated = get_migrated(main_target_uuid)
        main_target_optifine_cape = optifine_cape(main_target_uuid)
        
        print(f'''    {Fore.BLUE}•{Fore.RESET} Username       : {target}
    {Fore.BLUE}•{Fore.RESET} Past Usernames : {main_target_past_usernames}
    {Fore.BLUE}•{Fore.RESET} User UUID      : {main_target_uuid}
    {Fore.BLUE}•{Fore.RESET} Migrated Acc   : {main_target_migrated}
    {Fore.BLUE}•{Fore.RESET} Optifine Cape  : {main_target_optifine_cape}
    {Fore.BLUE}•{Fore.RESET} NameMC         : https://namemc.com/profile/{target}
''')


    else:
        print("Error fetching main target UUID (breaking/return)")
