num=float(input('Введите число: '))
if num >= 0 :
    print(repr(int(num))+' руб. '+("%.0f" %(100*(num-int(num))))+' коп.')
else:
    print ('Неккоректный формат')
