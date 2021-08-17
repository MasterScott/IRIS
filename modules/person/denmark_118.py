import requests
import bs4

from iris.module import Module
from iris.util import PrintUtil, HTMLUtil
from iris.logger import Logger


class IRISModule(Module):

    description = 'Lookup Danish citizens\' personal information by name/address/phone number'
    author = 'cs'
    date = '26-07-2021'

    def execute(self, name__address__phone_number: str):
        people = [x for x in self.__118_lookup(name__address__phone_number) if not all(list(map((lambda x : x is None), x)))]

        if len(people) == 0:
            raise Exception('No results found')

        people_sorted = []

        for person in people:
            name, address, phone = person

            for i, (name1, address1, phones) in enumerate(people_sorted.copy()):
                if name == name1 and address == address1:
                    if not phone in phones:
                        people_sorted[i][2].append(phone)
                    break
            else:
                people_sorted.append((name, address, [phone]))

        for name, address, phones in people_sorted:
            Logger.info(name + ':')

            PrintUtil.pp({
                'Address': address,
                'Phone' if len(phones) == 1 else 'Phone numbers': phones[0] if len(phones) == 1 else phones
            })
            Logger.nl()

        return True

    def __118_lookup(self, keywords):
        MAX_RESULTS = 25

        res = requests.get(
            'https://118.dk/search/go',
            params={
                'pageSize': MAX_RESULTS,
                'what': keywords,
            }
        )

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for i in range(MAX_RESULTS):
            target = soup.find('div', {'id': f'listing{i}'})

            if target is None:
                break
            
            name = HTMLUtil.get_element_string(target, 'h3', 'a')
            address = HTMLUtil.get_element_string(target, ('div', {'class': 'description-block'}), 'a')
            phone = HTMLUtil.get_element_string(target, 'p', 'a')

            yield name, address, phone

        return None, None, None
