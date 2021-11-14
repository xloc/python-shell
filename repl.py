import sys
import tty

stdin = sys.stdin
fd = stdin.fileno()
tty.setraw(fd)

while True:
    ch = stdin.read(1)
    print(f'{ch!r}', end='\r\n')
    if ch == '\x03':
        break

print('=== END ===')
