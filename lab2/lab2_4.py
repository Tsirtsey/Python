"""
Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла, найти в нем с 
помощью регулярных выражений все подстроки определенного вида, в соответствии с вариантом. 
Например, для варианта № 1 скрипт должен вывести на экран следующее:
Строка 3, позиция 10 : найдено '11-05-2014' Строка 12, позиция 2 : найдено '23-11-2014' Строка 12, позиция 17 : найдено '23-11-2014'


Вариант 5: найдите все номера телефонов – подстроки вида «(000)1112233» или «(000)111-22-33».
"""


import re  
file=open('lab2_4.txt','r') 
text=file.read() 
file.close() 
line=text.split("\n") 
p = re.compile('(\b?\(\d{3}\)\d{7}\b?)|(\b?\(\d{3}\)\d{3}-\d{2}-\d{2}\b?)')
for i in range(len(line)):
    a=re.search(p,line[i]) 
    if a!=None: 
        print('Строка:',i+1,'Позиция:',a.span()[0]+1)        