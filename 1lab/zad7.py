adr=input('Введите адрес: ')
list=adr
i=0
j=0
t=0
str=''
while i<len(list):
    str+=list[i]
    if list[i]=='.':
        t+=1
    if (str=='www.'):
        j=1
    if t==2:
        str=str+'com'
        break
    i+=1
if j==1:
    str='http://'+str[4:]
print(str)