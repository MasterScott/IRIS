import requests
import bs4

from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):
    description = 'Get social media profiles on linktr.ee by username'
    author = 'cs'
    date = '31-08-2021'

    def execute(self, username: str):
        res = requests.get(f'https://linktr.ee/{username}')

        if res.status_code == 404:
            raise Exception('Profile not found')

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        username = soup.find('meta', {'property': 'profile:username'})['content']
        avatar_url = soup.find('meta', {'property': 'og:image'})['content']
        profile_url = soup.find('meta', {'property': 'og:url'})['content']

        links = []

        for link_tag in soup.find_all('a', {'data-testid': 'LinkButton'}):
            url = link_tag['href']
            name = link_tag.find('p').text

            links.append([url, name])
        
        PrintUtil.pp({
            'Username': username,
            'Avatar': avatar_url,
            'Profile': profile_url,
            'Links': links,
        })