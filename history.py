import yaml
import os


class History:
    def __init__(self, path):
        self.path = path
        self.records = self._load_history(path)

    @staticmethod
    def _load_history(path):
        path = os.path.expanduser(path)
        if not os.path.exists(path) or not os.path.isfile(path):
            return []

        with open(path) as f:
            items = yaml.load(f, Loader=yaml.Loader)

        return items if items is not None else []

    def add(self, cmd):
        self.records.append(dict(cmd=cmd))

    def lookup(self, input, offset=0):
        for item in self.records[::-1]:
            cmd = item['cmd']
            if cmd.startswith(input):
                if offset == 0:
                    return cmd
                else:
                    offset -= 1

    def save(self, path=None):
        path = self.path if path is None else path
        with open(path, 'w') as f:
            yaml.dump(self.records, f)

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        return self.records.__getitem__(idx)


def test():
    HISTORY_PATH = './.history'

    h = History(HISTORY_PATH)
    h.add('less .history')
    h.add('vi .history')
    h.save()

    print(f'history entries {len(h)}')
    for i in h[-5:]:
        print(i)

    print(h.lookup('vi'))
    print(h.lookup('less'))
    print(h.lookup('a'))
    print(h.lookup('b'))
    print(h.lookup('b', offset=1))
