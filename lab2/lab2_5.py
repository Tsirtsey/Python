"""
Введите с клавиатуры текст. 
Программно найдите в нем и выведите отдельно все слова, 
которые начинаются с большого латинского символа (от A до Z) 
и заканчиваются 2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002». 
Используйте регулярные выражения.
"""


import re
text=input('Введите текст: ')
result=re.findall(r'[A-Z][a-z]+[0-9]{2,4}\b',text)
print(result)