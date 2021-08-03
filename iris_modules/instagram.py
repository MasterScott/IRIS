import sys
import colorama
import argparse,json
import httpx,hmac,hashlib,urllib
import requests
import os
from httpx import get
from colorama import Fore, Back, Style, init

colorama.init(autoreset=True)
sessionsId = json.load(open('config.json'))['instagram_sessionID']

def getUserId(target,sessionsId):
    cookies = {'sessionid': sessionsId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96',}
    r = get('https://www.instagram.com/{}/?__a=1'.format(target),headers=headers, cookies=cookies)
    try:
        info = json.loads(r.text)
        id = info["logging_page_id"].strip("profilePage_")
        return({"id":id,"error":None})
    except :
        return({"id":None,"error":"User not found or rate limit"})

def getInfo(target,sessionId):
    userId=getUserId(target,sessionId)
    if userId["error"]!=None:
        return({"user":None,"error":"User not found or rate limit"})
    else:
        cookies = {'sessionid': sessionId}
        headers = {'User-Agent': 'Instagram 64.0.0.14.96',}
        response = get('https://i.instagram.com/api/v1/users/'+userId["id"]+'/info/', headers=headers, cookies=cookies)
        info = json.loads(response.text)
        infoUser = info["user"]
        infoUser["userID"]=userId["id"]
        return({"user":infoUser,"error":None})

def advanced_lookup(target):
    USERS_LOOKUP_URL = 'https://i.instagram.com/api/v1/users/lookup/'
    SIG_KEY_VERSION = '4'
    IG_SIG_KEY = 'e6358aeede676184b9fe702b30f4fd35e71744605e39d2181a34cede076b3c33'

    def generate_signature(data):
        return 'ig_sig_key_version=' + SIG_KEY_VERSION + '&signed_body=' + hmac.new(IG_SIG_KEY.encode('utf-8'),data.encode('utf-8'),hashlib.sha256).hexdigest() + '.'+ urllib.parse.quote_plus(data)

    def generate_data( phone_number_raw):
        data = {'login_attempt_count': '0',
                'directly_sign_in': 'true',
                'source': 'default',
                'q': phone_number_raw,
                'ig_sig_key_version': SIG_KEY_VERSION
                }
        return data

    data=generate_signature(json.dumps(generate_data(target)))
    headers={
    "Accept-Language": "en-US",
    "User-Agent": "Instagram 101.0.0.15.120",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "X-FB-HTTP-Engine": "Liger",
    "Connection": "close"}
    try:
        r = httpx.post(USERS_LOOKUP_URL,headers=headers,data=data)
        rep=r.json()
        return({"user":rep,"error":None})
    except:
        return({"user":None,"error":"rate limit"})


def main(target, sessionsId):
    print(f'{Fore.YELLOW}•{Fore.RESET} Grabbing {target}\'s infomation...\n')
    infos = getInfo(target, sessionsId)
    if infos["user" ]== None:
        print(infos["error"])

    else:
        print(f'{Fore.GREEN}•{Fore.RESET} Simple Scan Complete')
        infos = infos["user"]

        if "public_email" in infos.keys():
            if infos["public_email"]!='':
                email = infos["public_email"]
            else:
                email = "None"
        else:
            email = "None"

        if "public_phone_number" in infos.keys():
            if str(infos["public_phone_number"])!='':
                phone = str(infos["public_phone_country_code"])+" "+str(infos["public_phone_number"])
            else:
                phone = "None"
        else:
            phone = "None"

        bio = infos["biography"].replace("\n", ", ")

        print(f'''    {Fore.BLUE}•{Fore.RESET} Username       : {infos["username"]}
    {Fore.BLUE}•{Fore.RESET} Full Name      : {infos["full_name"]}
    {Fore.BLUE}•{Fore.RESET} Verifed Acc    : {infos["is_verified"]}
    {Fore.BLUE}•{Fore.RESET} Followers      : {infos["follower_count"]}
    {Fore.BLUE}•{Fore.RESET} Following      : {infos["following_count"]}

    {Fore.BLUE}•{Fore.RESET} Post Count     : {infos["media_count"]}
    {Fore.BLUE}•{Fore.RESET} Account Bio    : {bio}

    {Fore.BLUE}•{Fore.RESET} Phone Number   : {phone}
    {Fore.BLUE}•{Fore.RESET} Email Address  : {email}
''')

        other_infos = advanced_lookup(target)
        print(f'{Fore.GREEN}•{Fore.RESET} Advanced Scan Complete')
        if other_infos["error"]=="rate limit":
            print("Rate limit please wait a few minutes before you try again")
        elif "message" in other_infos["user"].keys():
            if other_infos["user"]["message"]=="No users found":
                print(f"{Fore.RED}•{Fore.RESET} Advanced Lookup did not work on this account")
            else:
                print(f"{Fore.RED}•{Fore.RESET} Rate limit please wait a few minutes before you try again.")
        else:
            if "obfuscated_email" in other_infos["user"].keys():
                if other_infos["user"]["obfuscated_email"]!='':
                    print(f"    {Fore.BLUE}•{Fore.RESET} Linked email    : "+other_infos["user"]["obfuscated_email"])
                else:
                    print(f"    {Fore.BLUE}•{Fore.RESET} Linked email    : No obfuscated email found")

            if "obfuscated_phone"in other_infos["user"].keys():
                if str(other_infos["user"]["obfuscated_phone"])!='':
                    print(f"    {Fore.BLUE}•{Fore.RESET} Linked Phone   : "+str(other_infos["user"]["obfuscated_phone"]))
                else:
                    print(f"    {Fore.BLUE}•{Fore.RESET} Linked Phone   : No obfuscated phone found")
        print()

def run(target):
    main(target, sessionsId)
