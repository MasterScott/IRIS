import requests, json

from iris.module import Module
from iris.util import PrintUtil
from iris.util import BoxUtil

class IRISModule(Module):

    description = 'Look up a email or username with the WeLeakInfo API'
    author = 'HellSec'
    date = '08-04-2021'

    def execute(self, email: str):
        try:
            results = []
            apiKey = json.load(open('config.json'))['weleakinfo_key']

            r = requests.get(f'https://api.weleakinfo.to/api?value={email}&type=email&key={apiKey}').json()
            for x in r['result']:
                sources = x["sources"]
                if len(sources) > 0:
                    sources = ', '.join(sources)
                else:
                    sources = 'Unknown Source'
                results.append([x['line'], sources])

            BoxUtil.boxify(
                [
                    {'Login': x, 'Database': db}
                    for x, db in results
                ],
                title='Lookup results',
                show_keys=True
            )
        except Exception as e:
            print(e)
