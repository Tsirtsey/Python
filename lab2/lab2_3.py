"""
Задан путь к директории с музыкальными файлами (в названии которых нет номеров, 
а только названия песен) и текстовый файл, хранящий полный список песен с 
номерами и названиями в виде строк формата «01. Freefall [6:12]». 
Напишите скрипт, который корректирует имена файлов в директории на основе текста списка песен.
"""


import os
os.chdir(r"C:\Users\Кирилл\Desktop\Новая папка\Программирование\Питон\2_laba\music")
list=os.listdir(r"C:\Users\Кирилл\Desktop\Новая папка\Программирование\Питон\2_laba\music")
i=0
newname=''
newnamelist=[]
file=open(r"C:\Users\Кирилл\Desktop\Новая папка\Программирование\Питон\2_laba\lab2_3.txt",'r')
text=file.read()
file.close()
text=text+'\n'
while i<len(text):
    newname+=text[i]
    if (text[i]==('\n')):
        newname=newname[:-1]
        newnamelist.append(newname)
        newname=''
    i+=1
i=0
while i<(len(list)-0):
    os.rename(list[i],newnamelist[i])
    i+=1  