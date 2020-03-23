nomer=input('Введите номер карты: ')
i=0
nom=''
str=''
while i<len(nomer):
    if nomer[i].isdigit():
        str+=nomer[i]
    i+=1
i=0    
if len(str)==16:
    while i<len(str):
        if i<4:
            nom+=str[i]
        if (i>=4)and(i<12):
            nom+='*'
        if i>11:
            nom+=str[i]
        if (i==3)or(i==7)or(i==11):
            nom+=' '
        i+=1
else:
    print('Введите 16 символов!')
    
print('Номер вашей карты: '+nom)