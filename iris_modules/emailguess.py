from colorama import Fore

def emailGuess(target, filename):
    guesses = []

    email_file = open(filename, 'r').readlines()

    provider = target.split('@')[1]
    for email in email_file:
        email = email.rstrip()
        if provider[0] == email[0]:
            if len(provider.split('.')[0]) == len(email.split('.')[0]):
                print(f'{Fore.YELLOW}•{Fore.RESET} Possible Email - {target.split("@")[0]}@{email}')
        
def run(target):
    emailGuess(target, 'emails.txt')