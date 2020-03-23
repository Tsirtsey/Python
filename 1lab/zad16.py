import random,time,datetime
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
dataN=datetime.datetime(2018,9,14,22,45)
match=''
i=0
while i<16:
    match+='Игра: '+teams[i]+' против '+teams[i+1]
    print(match,time.strftime("%d/%m/%Y %H:%M"))
    match=''
    time=dataN+datetime.timedelta(days=7*i)
    i+=2