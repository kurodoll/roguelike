from colorama import init, Fore, Style

init()  # colorama


def log(caller, message):
    print(f'[{Fore.YELLOW}' + caller + f'{Style.RESET_ALL}] ' + message)
