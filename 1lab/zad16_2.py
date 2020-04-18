"""
Напишите скрипт, который на основе списка из 16 названий
футбольных команд случайным образом формирует 4 группы по 4
команды, а также выводит на консоль календарь всех игр (игры
должны проходить по средам, раз в 2 недели, начиная с 14 сентября
текущего года). Даты игр необходимо выводить в формате «14/09/2016,
22:45». Используйте модули random и itertools.

"""

import random,time,datetime
from itertools import count


teams = ['Россия','Испания','ОАЭ','Нидерланды', 'Англия', 'Германия', 'Швеция', 'Дания', 
         'ДНР', 'ЛНР', 'Украина', 'Бразилия', 'Япония', 'Урлай', 'Грузия','Португалия']


random.shuffle(teams)
print('Команда 1: ')
for i in range(0,4):
    print(teams[i])
print()
print('Команда 2: ')
for i in range(4,8):
    print(teams[i])
print()
print('Команда 3: ')
for i in range(8,12):
    print(teams[i])
print()
print('Команда 4: ')
for i in range(12,16):
    print(teams[i])
print()


random.shuffle(teams)
razn=datetime.timedelta(days=14)
dataN=datetime.datetime(2020,9,14,22,45)
match=''
for i in count(0, 2):
    if i>=16:
        break
    match+='Игра: '+teams[i]+' против '+teams[i+1]
    print(match,time.strftime("%d/%m/%Y %H:%M"))
    match=''
    time=dataN+datetime.timedelta(days=7*i)
