import requests, json

from iris.module import Module
from iris.util import PrintUtil
from iris.util import BoxUtil

class irisModule(Module):

    description = 'Scrape all members from a Discord server'
    author = 'HellSec'
    date = '08-14-2021'

    def execute(self, channelID: str):
        print()

        results  = []

        database = open('data.json', 'a')
        token    = json.load(open('config.json'))['discord_token']

        endpoint = f'https://discord.com/api/v9/channels/{channelID}/messages?limit=100'

        req = requests.get(url=endpoint, headers={'authorization': token}).json()
        for log in req:
            serverid    = log['id']
            av          = log['author']['avatar']
            username    = log['author']['username'] +'#'+ log['author']['discriminator']
            userid      = log['author']['id']
            message     = log['content']

            if av == None or av == 'None':
                avatar = f'None'
            else:
                avatar = f'https://cdn.discordapp.com/avatars/{userid}/{av}.webp'
                
            results.append([serverid, username, avatar])

        BoxUtil.boxify(
            [
                {'Server': serverid, 'Username': user, 'Avatar Hash': av}
                for serverid, user, av in results
            ],
            title='Scrape Results',
            show_keys=True
        )
