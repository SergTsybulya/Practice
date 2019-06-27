# -*- coding: utf-8 -*-

import re
import argparse
from time import sleep
from termcolor import colored

m = 0
exit_command = ['q', 'Q', 'quit', 'Quit', 'exit', 'Exit']


parser = argparse.ArgumentParser()

parser.add_argument('-b', action='store_true')
args, _ = parser.parse_known_args()


def help():
    print(f"""
        Команда может быть любая математическая операция.
        Пример:""", colored(" 2 + 2", "blue"), """или""", colored("4* 100", "blue"), """.
        Команда""", colored("mem", 'blue'), """сохраняет последний результат.
        Для использования сохраненного результата подставьте переменную""", colored("m", "blue"), """.
        Команда для выхода:""", colored(" ".join(exit_command), "blue"), """.
    """)


def printProgressBar (iteration, total, prefix='', suffix='', decimals=1, length=100, fill=r'█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def loading(num=4):
    if args.b:
        return
    items = list(range(num))
    l = len(items)
    printProgressBar(0, l, prefix='Прогресс:', suffix='Старт', length=50)
    for i, item in enumerate(items):
        sleep(0.2)
        check = 'Проверка'
        if i == num - 1:
            check = 'Выполненно'
        printProgressBar(i + 1, l, prefix='Прогресс:', suffix=check, length=50)




def boot():
    print("Запуск программы...")
    loading(3)
    print("Наличие у пользователя мозгов..")
    loading(25)
    print("Уровень:", end="")
    print(colored(" Допустимо", "yellow"))
    print("Проверка радиуса рук пользователя..")
    loading(18)
    print("Кривизна:", end="")
    print(colored(" Ок", "green"))
    print("Положения рук пользователя относительно тела..")
    loading(6)
    print("Позиция:", end="")
    print(colored(" Ок", "green"))
    print("Загрузка пакетов и финальная компиляция..")
    loading(3)
    print('Для помощи используйте комманду', colored("help.", "blue"))


if __name__ == '__main__':
    boot()
    while 1:
        try:
            pattern = r'^([0-9]?[m]*3?)(\s*?[+-/*%]?[//]?\s*?([0-9]?[m]*3?))*$'
            command = input('Команда: ')
            if command == 'help':
                help()
            if command in exit_command:
                print('Завершение программы...')
                print(colored('Прощай человек', "red"))
                loading()
                break
            if re.match(pattern, command) is not None:
                result = eval(command)
                _m = result
                print("Ответ: ", colored(result, "blue"))
            if command == 'mem':
                m = _m
        except ZeroDivisionError:
            print(colored('\nДеление на 0!', 'red'))
            continue
        except NameError:
            print(colored('Что-то пошло не так. Я умираю из-за тебя, человек..', "red"))
            break
        except Exception as error:
            print(colored(f'\nНеизвестная ошибка: {error}', "red"))
            continue
# Calc for fun
