list = [1,2,3]
x = 0
for i in range(len(list)):
    if list[i] > x:
        x = list[i]
    else:
        x = 0
        break
if x == 0:
    print ("FALSE")
elif x!= 0:
    print ("TRUE")
