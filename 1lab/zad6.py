text=input("Enter the text: ")
def simbols():
    string = text.lower()
    simbol = str(string)
    for i in range (len(simbol)):
        if simbol.count(simbol[i]) == 1:
            print(simbol[i], end = " ")
            
simbols()