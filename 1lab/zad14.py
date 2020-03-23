def non_empty(func):
    def dec():
        res = func()
        count = 0
        for i in res:
            if i == '' or i == None:
                res.pop(count)
            count+=1
        return res
    return dec

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1',None]

print(get_pages())