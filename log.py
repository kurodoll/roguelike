from colorama import init, Fore, Style

init()  # colorama


def log(caller, message, msg_type=None):
    if msg_type == 'error':
        print(f'[{Fore.RED}', end='')
    elif msg_type == 'warning':
        print(f'[{Fore.YELLOW}', end='')
    else:
        print(f'[{Fore.GREEN}', end='')

    print(caller + f'{Style.RESET_ALL}] ' + message)
