import requests
import base64
import time
import re

from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):

    description = 'Get Keybase account information by username'
    author = 'cs'
    date = '10-07-2021'

    def execute(self, username: str):
        res = requests.get('https://keybase.io/_/api/1.0/user/lookup.json', params={'username': username})

        if res.status_code != 200:
            raise Exception('User not found')

        try:
            profile = res.json()['them']
        except KeyError:
            raise Exception('User not found')

        id = profile.get('id')
        username = profile.get('basics', {}).get('username')
        creation_date = profile.get('basics', {}).get('ctime')
        full_name = profile.get('profile', {}).get('full_name')
        location = profile.get('profile', {}).get('location')
        bio = profile.get('profile', {}).get('bio')
        profile_picture = profile.get('pictures', {}).get('primary', {}).get('url')

        btc_addr = profile['cryptocurrency_addresses'].get('bitcoin', [{}])[0].get('address')
        zcash_addr = profile['cryptocurrency_addresses'].get('zcash', [{}])[0].get('address')

        try:
            public_key = profile.get('public_keys', {}).get('primary', {}).get('bundle', '').split('\n\n')[1].split('-----')[0]

            emails = self.__get_emails_from_public_key(public_key)
        except IndexError:
            public_key = None
            emails = None

        devices = []

        for device_info in profile['devices'].values():
            creation_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(device_info['ctime']))
            devices.append({'Name': device_info['name'], 'Type': device_info['type'], 'Creation date': creation_date})

        try:
            stellar_acc_id = profile['primary']['account_id']
        except KeyError:
            stellar_acc_id = None

        PrintUtil.pp({
            'Username'          : username,
            'ID'                : id,
            'Creation date'     : creation_date,
            'Full name'         : full_name,
            'Location'          : location,
            'Emails'            : emails,
            'Bio'               : bio,
            'Bitcoin address'   : btc_addr,
            'ZCash address'     : zcash_addr,
            'Profile picture'   : profile_picture,
            'Stellar account ID': stellar_acc_id,
            'Devices'           : devices,
            #'Public key'       : public_key
        })

    def __get_emails_from_public_key(self, public_key):
        return re.findall(r'\s<(.*?)>', str(base64.b64decode(public_key)))
