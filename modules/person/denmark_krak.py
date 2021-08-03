import requests
import json
import re

from iris.module import Module
from iris.util import PrintUtil
from iris.logger import Logger


class IRISModule(Module):

    description = 'Lookup Danish citizens\' personal information by name/address/phone number'
    author = 'cs'
    date = '26-07-2021'

    def execute(self, name__address__phone_number: str):
        for fn in (self.__krak_lookup, self.__krak_lookup_address):
            people = [_ for _ in fn(name__address__phone_number)]

            if len(people) > 0:
                break

        if len(people) == 0:
            raise Exception('No results found')

        for name, addresses, phones in people:
            if name is None:
                break

            if len(addresses) == len(phones) == 0:
                continue

            Logger.info(name + ':')
            PrintUtil.pp({
                'Address' if len(addresses) == 1 else 'Addresses': addresses[0] if len(addresses) == 1 else addresses,
                'Phone' if len(phones) == 1 else 'Phone numbers': phones[0] if len(phones) == 1 else phones
            })
            Logger.nl()

        return True

    def __krak_lookup(self, keywords):
        res = requests.get(
            'https://www.krak.dk/api/ps',
            params={
                'query': keywords,
                'sortOrder': 'default',
                'profile': 'krak',
                'page': 1,
                'lat': 0,
                'lng': 0,
                'limit': 25,
                'client': True
            },
            headers={
                'Content-Type': 'application/json'
            }
        )

        if res.status_code != 200:
            raise Exception('An error occurred')

        for person in res.json()['items']:
            name = person['name']
            addresses = [address['streetName'] + ' ' + address['streetNumber'] + ', ' + address['postArea'] + ' ' + address['postCode'] for address in person.get('address', [])]
            phones = [x['phoneNumber'] for x in person.get('phoneNumbers', [])]

            yield name, addresses, phones

        return None, None, None

    def __krak_lookup_address(self, address):
        res = requests.get(
            'https://mapsearch.eniro.com/search/search.json',
            params={
                'callback': 'jQuery21105051293404342361_1627338229099',
                'phase': 'first',
                'index': 'wp',
                'profile': 'dk_krak',
                'q': address,
                'reverseLookup': True,
                'center': '12.519760628152255,55.96476667987731',
                'zoom': 14,
                'sortOrder': 'default',
                'viewPx': '588,893',
                'adjPx': '0,0,0,0',
                'pageSize': 25,
                'version': 4,
                'offset': 0
            },
            headers={
                'Content-Type': 'application/javascript'
            }
        )

        if res.status_code != 200:
            raise Exception('An error occurred')

        json_data_match = re.search(r'^jQuery21105051293404342361_1627338229099\((.*)\);$', res.text)
        
        if json_data_match is None:
            raise Exception('JSON data not found')

        json_data = json.loads(json_data_match.group(1))

        for person in json_data['search']['wp']['features']:
            name = person['name'].replace('  ', ' ')
            addresses = [address['label'] + ', ' + address['area'] + ' ' + address['postcode'] for address in person.get('addresses', [])]
            phones = person.get('phoneNumbers', [])

            yield name, addresses, phones

        return None, None, None
