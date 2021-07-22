import requests

def run(target):
    if '@' not in target:
        print(f'    {Fore.RED}•{Fore.RESET} Non-Email Skipping Module')
        return

    endpoint = 'https://api.twitter.com/i/users/email_available.json?email={target}&send_error_codes=1'