import codecs
import random
from pathlib import Path

first = 'Мама мыла раму'
second = 'Рамена мало было'
lf = lambda x, y: x == y
l = list(map(lf, first, second))
print(l)


def get_advanced_writer(file_name):
    Path(file_name).touch()

    def write_everything(*data_set):
        with codecs.open(file_name, 'w', 'utf-8') as file:
            a = [str(x) + '\n' for x in data_set]
            for x in a:
                file.write(x)

    return write_everything


class MysticBall:
    def __init__(self,*args):
        self.words = args
    def __call__(self):
        try:
            return random.choice(self.words)
        except Exception as e:
            print(e)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
