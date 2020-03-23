import random
kolvo=random.randint(0,100)
print('Количество элементов: '+str(kolvo))
mas=[]
for i in range(kolvo):
    mas.append(random.randint(0,9))
print(mas)
for i in range(kolvo**2):
    if (2**i)>kolvo:
        break
nol=(2**i)-kolvo
for i in range(nol):
    mas.append(0)
print(mas)