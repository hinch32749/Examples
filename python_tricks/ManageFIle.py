# Поддержка инструкции with в собственных объектах
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        print('opening')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print('closing')
            self.file.close()


with ManagedFile('new_file.txt') as f:
    print('====')
    f.write('Hello world!\n')
    f.write('and now, good bye!')

print('end')

for line in open('new_file.txt'):
    print(line)