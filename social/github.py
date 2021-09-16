import requests

from iris.module import Module
from iris.util import PrintUtil


class IRISModule(Module):

    description = 'Get GitHub account information by username'
    author = 'cs'
    date = '10-07-2021'

    def execute(self, username: str):
        res = requests.get(f'https://api.github.com/users/{username}', headers={'Accept': 'application/vnd.github.v3+json'})

        profile = res.json()

        if profile.get('message') is not None:
            raise Exception('Profile not found')

        PrintUtil.pp({
            'Name'          : profile.get('name'),
            'Handle'        : profile.get('login'),
            'ID'            : profile.get('id'),
            'Company'       : profile.get('company'),
            'Website'       : 'http://' + profile.get('blog').lower() if profile.get('blog') else None,
            'Location'      : profile.get('location'),
            'Email'         : profile.get('email'),
            'Bio'           : profile.get('bio').replace('\n', '\\n') if profile.get('bio') else None,
            'Twitter'       : ('https://twitter.com/' + profile.get('twitter_username')) if profile.get('twitter_username') else None,
            'Created at'    : profile.get('created_at'),  # TODO: parse date
            'Updated at'    : profile.get('updated_at'),  # TODO: parse date
            'Followers'     : profile.get('followers'),
            'Following'     : profile.get('following'),
            'Profile link'  : profile.get('html_url')
        })
