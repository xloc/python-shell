import datetime
import os


def pwd():
    pwd = os.environ['PWD']
    home = os.environ['HOME']
    if pwd.startswith(home):
        return pwd.replace(home, '~', count=1)
    else:
        return pwd


def time(format=r"%H:%M:%S"):
    now = datetime.datetime.now()
    return now.strftime(format)


def date(format=r"%Y/%m/%d"):
    now = datetime.datetime.now()
    return now.strftime(format)


def hostname():
    return os.uname()[1]


def user():
    return os.environ['USER']


def test_all():
    for fn in [pwd, time, date, hostname, user]:
        print(fn())


if __name__ == '__main__':
    test_all()
