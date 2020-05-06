"""
Напишите скрипт, позволяющий искать в заданной директории и в ее подпапках 
файлы-дубликаты на основе сравнения контрольных сумм (MD5). Файлы могут 
иметь одинаковое содержимое, но отличаться именами. Скрипт должен вывести 
группы имен обнаруженных файлов-дубликатов.
"""


import os 
import hashlib 
 
ellist=os.walk(r'C:\Users\Кирилл\Desktop\Новая папка\Программирование\Питон\2_laba') 
filelist=[] 
filecount=[] 
for el in ellist: 
    if el[1]!=0: 
        for e in el[2]: 
            filelist.append(el[0]+'\\'+e) 
 
for file in filelist: 
    with open(file, 'rb') as f: 
        content = f.read() 
        f.close() 
        filecount.append(hashlib.md5(content).hexdigest()) 
 
for i in range(0,len(filelist)-1): 
    for j in range(i+1,len(filelist)): 
        if filecount[i]==filecount[j]: 
            print(filelist[i],'=',filelist[j])