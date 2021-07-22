


modules = [
        [0, 'Set-Target-<TARGET>', 'Set the target for IRIS.', 'target, set'],
        [1, 'Start-<Module>', 'Search for keybase\'s account email.', 'start, modules, execute'],
        [2, 'Search <KEYWORD>', 'Search for any command based on keywords.', 'search, interactive, keywords'],
        [3, 'Clear', 'Clear all infomation from the screen.', 'clear, cls'],
        [4, 'Help', 'Shows This Help Message.', 'help, modules, infomation']
]

mj = [  
        [1, 'Breach', 'Scan an email for breaches, leaks, and sites the email is active on', 'search, online, email, breach, leak'],
        [2, 'SiteScan', 'Scan various online websites that a user may be signed up on', 'online, email, social, api'],
        [3, 'WeLeakInfo', 'Wrapper for weleakinfo.to to find recent breaches on a targets email', 'online, email, interactive, api'],
        [4, 'Thatsthem', 'Online scan for full name, phone number, and address', 'online, email, interactive, api'],
        [5, 'Twitter', 'Grabs the full email address and phone number of a target account', 'online, email, interactive, api, twitter, leak'],
]


def run(keyword):
    print(f'Searching for {keyword}')