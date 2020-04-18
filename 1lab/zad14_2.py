"""
Напишите декоратор non_empty, который дополнительно проверяет
списковый результат любой функции: если в нем содержатся пустые
строки или значение None, то они удаляются. Пример кода:
@non_empty
def get_pages():
 return ['chapter1', '', 'contents', '', 'line1']
 
"""

def non_empty(func):
    def dec():
        ent = func()
        print(ent)
        res = list(filter(None, ent))
        return res
    return dec

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1',None]

print(get_pages())