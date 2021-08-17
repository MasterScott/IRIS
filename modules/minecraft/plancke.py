import requests
import bs4
import re

from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):

    description = 'Get Plancke account information by Minecraft username/UUID'
    author = 'cs'
    date = '10-07-2021'

    def execute(self, username__uuid: str):
        SOCIAL_MEDIA = [
            'TWITTER',
            'YOUTUBE',
            'TWITCH',
            'HYPIXEL'
        ]

        res = requests.get(f'https://plancke.io/hypixel/player/stats/{username__uuid}')

        if res.status_code == 404:
            raise Exception('Player not found')

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        profile = {'social_media': {}}

        # * get profile link
        profile_link = res.url

        profile.update({'profile_link': profile_link})

        # * get username
        title_html = soup.find('title')
        username_re = re.search(r'(.+?)\'(s|) Stats', title_html.string)
        username = username_re.group(1).strip().strip(' ')

        profile.update({'username': username})

        # * get social media
        for social_media_name in SOCIAL_MEDIA:
            a_html = soup.find('a', id='social_' + social_media_name)

            if a_html:
                social_media_url = a_html.get('href')

                if social_media_url:
                    profile['social_media'].update({social_media_name.lower(): social_media_url})

        for x in soup.find_all('script'):
            if x.string:

                # * get Discord
                discord_re = re.search(r'swal\(".*\'s Discord", "(.+?)"\)', x.string, re.MULTILINE)

                if discord_re:
                    discord = discord_re.group(1)
                    profile.update({'discord': discord})

                # * get uuid    
                uuid_re = re.search(r'var uuid = \'(.+?)\';', x.string)

                if uuid_re:
                    uuid = uuid_re.group(1)
                    profile.update({'uuid': uuid})

        profile_social_media = profile.get('social_media', {})
        social_media = [[profile_social_media[x], x] for x in profile_social_media] if profile_social_media else []

        PrintUtil.pp({
            'Username'      : profile.get('username'),
            'UUID'          : profile.get('uuid'),
            'Discord'       : profile.get('discord'),
            'Profile link'  : profile.get('profile_link'),
            'Social media'  : social_media
        })
