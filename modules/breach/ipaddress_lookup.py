import requests
import json

from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):
    description = 'Look up an IP address with the Breach Directory API'
    author = 'HellSec'
    date = '08-08-2021'

    def execute(self, ipaddress_hostname: str):
        print()
        req = requests.post(url=f'https://breachdirectory.com/api_usage?domain=https://test.com&method=ip&query={ipaddress_hostname}').text
        r = req.replace('API provided by BreachDirectory.', '')
        r = json.loads(f'[{r.replace("}", "}, ")}]'.replace('\n', '').replace('}, ]', '}]'))
        
        if 'subscriptable' in req.lower():
            PrintUtil.pp({
                'Error': str(r)
            })
            return

        for result in r:
            email = result['email']
            ip = result['ip']
            domain = result['title']
            username = result['username']

            if ip == '': ip = 'None'
            if email == '': email = 'None'
            if domain == '': domain = 'None'
            if username == '': username = 'None'

            PrintUtil.pp({
                'Email'         : email,
                'Username'      : username,
                'IP Address'    : ip,
                'Domain'        : domain
            })
            print()
