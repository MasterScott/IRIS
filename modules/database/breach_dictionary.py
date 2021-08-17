import requests, json
from iris.module import Module
from iris.util import PrintUtil
from iris.util import BoxUtil


class IRISModule(Module):

    description = 'Look up an email or username with the Breach Directory API'
    author = 'HellSec'
    date = '08-07-2021'

    def execute(self, username_email: str):
        print()
        if '@' in username_email:
            method = 'email'
        else:
             method = 'username'

        req = requests.post(url=f'https://breachdirectory.com/api_usage?domain=https://test.com&method={method}&query={username_email}').text
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
