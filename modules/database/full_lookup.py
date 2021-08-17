import requests, json
from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):

    description = 'Lookup using all API\'s that are available, WLI, BD, And Breacher'
    author = 'HellSec'
    date = '08-11-2021'

    def execute(self, username_email: str):
        print()

        results = []

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

        for result in r:
            email = result['email']
            ip = result['ip']
            domain = result['title']
            username = result['username']

            PrintUtil.pp({
                'Email':            email,
                'IP Address':       ip,
                'Domain Target':    domain,
                'API':              'Breach Directory'
            })

            print()


        try:
            apiKey = json.load(open('config.json'))['weleakinfo_key']

            r = requests.get(f'https://api.weleakinfo.to/api?value={email}&type=email&key={apiKey}').json()
            for x in r['result']:
                sources = x["sources"]
                if len(sources) > 0:
                    sources = ', '.join(sources)
                else:
                    sources = 'Unknown Source'
                results.append({
                    'Email':            x['line'], 
                    'Domain Target':    sources,
                    'API':              'WeLeakInfo'
                })

        except Exception as e:
            print(e)


        PrintUtil.pp(
            results
        )