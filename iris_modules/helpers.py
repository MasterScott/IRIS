import sys

def modules():
    '''
        Basic help menu for Iris and all search tools
        ex : python3 {sys.argv[0]} -m help
    '''

    modules = [
        [1, 'Keybase', 'Search for keybase\'s account email.', 'keybase, search, online'],
        [2, 'Breach', 'Scan an email for breaches, leaks, and sites the email is active on', 'search, online, email, breach, leak'],
        [3, 'SiteScan', 'Scan various online websites that a user may be signed up on', 'online, email, social, api'],
        [4, 'WeLeakInfo', 'Wrapper for weleakinfo.to to find recent breaches on a targets email', 'online, email, interactive, api'],
        [5, 'Thatsthem', 'Online scan for full name, phone number, and address', 'online, email, interactive, api'],
        [6, 'Twitter', 'Grabs the full email address and phone number of a target account', 'online, email, interactive, api, twitter, leak']
        [7, 'Instagram', 'Grabs the name, public emails, and phone numbers of a target account', 'online, email, interactive, api, twitter, leak']
        [8, 'Minecraft', 'Return the basic infomation of a target account including past accounts and links', 'online, email, interactive, api, twitter, leak']
        [9, 'Discord', 'Grab infomation about a Discord account such as email, username, id, nitro status, and connections', 'online, email, interactive, api, twitter, leak']
    ]

    print(f'''
Basic help menu for Iris and all search tools
    - ex : 
        python3 {sys.argv[0]} -m help
''')
    for module in modules:
        print(
        f'{module[1]}\n',
        f'\tDescriptor : {module[2]}\n',
        f'\tKeywords  : {module[3]}\n',
)