text=input('Введите текст: ')+(' ')
i=0
word=0
word8=''
word47=''
word4=''
str=''
sl=''
while i<len(text):
    if (text[i].isalnum())or(text[i]==(' ')):
        str+=text[i]  
    i+=1
i=0
while i<len(str):
    word=word+1
    sl=sl+str[i]
    if str[i]==' ':
        if word>8:
            word8=word8+sl+' '
            sl=''
            word=0
        elif (word<=8)and(word>=5):
            word47=word47+sl+' '
            sl=''
            word=0
        else:
            word4=word4+sl+' '
            sl=''
            word=0
    i=i+1
print('\n'+'Слова больше 7 букв:  '+word8+'\n'+'\n'+'Слова от 4 до 7 букв:  '+word47+'\n'+'\n'+'Слова меньше 4 букв:  '+word4)