from iris.module import Module
from iris.util import BoxUtil, DuckDuckGo


class IRISModule(Module):
    description = 'Enter a name and find Instagram profiles'
    author = 'HellSec'
    date = '08-11-2021'

    def execute(self, keywords: str):
        results = DuckDuckGo.search(f'site:instagram.com "{keywords}"')

        if len(results) == 0:
            raise Exception('No results found')

        def __check(keyword, url):
            """ Validate search result """
            if 'instagram.com' in url:
                if not keyword.lower() in url.lower():
                    return False
            return True

        BoxUtil.boxify(
            [
                {'Title': title, 'URL': url}
                for url, title in results
                if __check(keywords, url) is True
            ],
            title = 'Instagrams found',
            show_keys = True,
            thicc_border = True
        )
