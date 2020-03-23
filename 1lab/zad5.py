text = input("Enter the text: ")
def strings(text):
    word = text.split()
    for i in range (len(word)):
        if(word[i].istitle()):
            print (word[i].upper(), end=" ")
        else:
            print(word[i], end = " ")
            
strings(text)
