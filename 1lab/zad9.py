#5550
summa=int(input('Введите сумму: '))
otvet=''
v5k=0
v1k=0
v500=0
v100=0
v50=0
v10=0
balance = 100000

v5k=int(summa/5000)
v1k=int((summa-(5000*v5k))/1000)
v500=int((summa-(5000*v5k)-(1000*v1k))/500)
v100=int((summa-(5000*v5k)-(1000*v1k)-(500*v500))/100)
v50=int((summa-(5000*v5k)-(1000*v1k)-(500*v500)-(100*v100))/50)
v10=int((summa-(5000*v5k)-(1000*v1k)-(500*v500)-(100*v100)-(50*v50))/10)
vm10=int(summa-(5000*v5k)-(1000*v1k)-(500*v500)-(100*v100)-(50*v50)-(10*v10))


if summa > balance:
    print ('В банкомате недостаточно средств. Баланс банкомата = ' + str (balance))
else:
    if v5k!=0:
        v5k=str(v5k)+'*5000 '
        otvet+=v5k 
    if v1k!=0:
        v1k=str(v1k)+'*1000 '
        otvet+=v1k
    if v500!=0:
        v500=str(v500)+'*500 '
        otvet+=v500
    if v100!=0:
        v100=str(v100)+'*100 '
        otvet+=v100
    if v50!=0:
        v50=str(v50)+'*50 '
        otvet+=v50
    if v10!=0:
        v10=str(v10)+'*10 '
        otvet+=v10
    if vm10!=0:
        print('Банкомат мелочь не выдаёт!')
    print(otvet)        