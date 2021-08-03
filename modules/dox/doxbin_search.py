from iris.module import Module

import requests
import bs4

from iris.util import BoxUtil


class IRISModule(Module):

    description = 'Lookup published doxxes from DoxBin site'
    author = 'cs'
    date = '16-07-2021'

    def execute(self, keywords: str):
        results = self.__ddg(f'site:doxbin.org "{keywords}"')

        if len(results) == 0:
            raise Exception('No results found')

        def __check(keyword, url):
            """ Validate search result """
            if 'doxbin.org/user' in url:
                if not keyword.lower() in url.lower():
                    return False
            return True

        BoxUtil.boxify(
            [
                {'Title': title, 'URL': url}
                for url, title in results
                if __check(keywords, url) is True
            ],
            title='Doxbin results',
            show_keys=True
        )

    def __ddg(self, search_query):
        """ DuckDuckGo search """
        def __search(q):
            return requests.post(
                'https://lite.duckduckgo.com/lite/',
                headers={
                    'accept': '*/*',
                    'origin': 'https://lite.duckduckgo.com',
                    'referer': 'https://lite.duckduckgo.com/',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36'
                },
                data={
                    'q': q,     # search query
                    'kl': None, # search language (None/wt-wt = global)
                    'dt': None  # search time
                }
            )

        res = __search(search_query)

        # DuckDuckGo crawler/dork detected check
        if res.status_code == 403:
            __search('cute cat')  # ez bypass heh
            return self.__ddg(search_query)

        if res.status_code != 200:
            raise Exception(res.text)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        return [
            (x['href'], x.text)
            for x in soup.find_all('a', {'rel': 'nofollow'})
        ]
