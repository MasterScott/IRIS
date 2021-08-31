from iris.module import Module
from iris.util import BoxUtil, DuckDuckGo


class IRISModule(Module):
    description = 'Lookup published doxxes from DoxBin site'
    author = 'cs'
    date = '16-07-2021'

    def execute(self, keywords: str):
        results = DuckDuckGo.search(f'site:doxbin.org "{keywords}"')

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
