"""
Напишите скрипт reorganize.py, который в директории --source создает две директории: Archive и Small. 
В первую директорию помещаются файлы с датой изменения, отличающейся от текущей даты на количество 
дней более параметра --days (т.е. относительно старые файлы). Во вторую – все файлы размером меньше 
параметра --size байт. Каждая директория должна создаваться только в случае, если найден хотя бы один
файл, который должен быть в нее помещен. Пример вызова:
reorganize --source "C:\TestDir" --days 2 --size 4096
"""


import os, datetime, shutil
def sort(source,days,size):
    if os.path.exists(source+'\\Archive'):
        shutil.rmtree(source+'\\Archive')        
    if os.path.exists(source+'\\Small'):
        shutil.rmtree(source+'\\Small')
    listfiles=[]
    now=datetime.datetime.now()
    folders=os.walk(source)
    for way,dirs,files in folders:
        for f in files:
            listfiles.append(way+'\\'+f)        
    for i in range(len(listfiles)):
        stat=datetime.datetime.fromtimestamp(os.stat(listfiles[i]).st_mtime)
        if ((now-stat).days)>days:
            if os.path.exists(source+'\\Archive')==False:
                os.mkdir(source+'\\Archive')
            shutil.copy(listfiles[i],source+'\\Archive')
        if os.stat(listfiles[i]).st_size<size:
            if os.path.exists(source+'\\Small')==False:
                os.mkdir(source+'\\Small')
            shutil.copy(listfiles[i],source+'\\Small')
    print(listfiles)


sort(r'C:\Users\Кирилл\Desktop\Новая папка\Программирование\Питон\2_laba\2.6',14,15000)