import info


class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def prompt():
    return '{user}@{host} {pwd} >'.format(
        user=info.user(),
        host=info.hostname(),
        pwd=Color.GREEN + info.pwd() + Color.RESET,
    )


if __name__ == '__main__':
    print(prompt())
