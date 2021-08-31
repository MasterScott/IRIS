import requests
import iris

from iris.module import Module
from iris.util import BoxUtil


class IRISModule(Module):
    description = 'Look up emails and usernames with WeLeakInfo\'s API'
    author = 'HellSec, cs'
    date = '04-08-2021'

    def execute(self, email__username: str):
        res = requests.get(
            'https://api.weleakinfo.to/api',
            params={
                'type': 'email',
                'value': email__username,
                'key': iris.__app__.config.APIKeys.weleakinfo
            }
        )

        json_data = res.json()

        error = json_data.get('error')

        if error is not None:
            raise Exception(error)

        results = []

        for r in json_data['result']:
            sources = ', '.join(r['sources']) if len(r['sources']) > 0 else 'Unknown Source'
            results.append([r['line'], sources])

        BoxUtil.boxify(
            [
                {'Login': x, 'Database': db}
                for x, db in results
            ],
            title='Lookup results',
            show_keys=True
        )