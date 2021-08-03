import requests.adapters
import fake_headers
import cfscrape
import bs4

from urllib3.util.ssl_ import create_urllib3_context

from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):

    description = 'Get Twitter account email and phone number from username'
    author = 'cs'
    date = '10-07-2021'

    def execute(self, username: str):
        class CustomAdapter(requests.adapters.HTTPAdapter):

            def init_poolmanager(self, *args, **kwargs):
                super(self.__class__, self).init_poolmanager(*args, ssl_context=create_urllib3_context(), **kwargs)

        PASSWORD_RESET_URL = 'https://twitter.com/account/begin_password_reset'

        headers = fake_headers.Headers(browser='chrome', os='win', headers=True).generate()

        scraper = cfscrape.create_scraper()
        scraper.mount('https://', CustomAdapter())

        # get CSRF token
        res = scraper.get(PASSWORD_RESET_URL, headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        authenticity_token = soup.input.get('value')

        # send password reset request
        data = {'authenticity_token': authenticity_token, 'account_identifier': username}

        res = scraper.post(PASSWORD_RESET_URL, cookies=res.cookies, data=data, headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # error check
        err = soup.find('div', attrs={'class': 'is-errored'})

        if err is not None and err.text == 'Please try again later.':
            raise Exception('You have been rate limited')

        # extract
        info = soup.find('ul', attrs={'class': 'Form-radioList'})

        if info is None:
            raise Exception('Failed to fetch profile information')

        info = info.findAll('strong')

        if len(info) == 2:
            phone = info[0].text
            email = info[1].text
        else:
            email = info[0].text
            phone = None

            if not '@' in email:
                phone = email
                email = None

        PrintUtil.pp({
            'Email': email,
            'Phone': phone
        })
