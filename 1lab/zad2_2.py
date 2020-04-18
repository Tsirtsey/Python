"""
Написать скрипт, который выводит на экран «True», если элементы
программно задаваемого списка представляют собой возрастающую
последовательность, иначе – «False».

"""

def isSortedArray(array):
	generator = (i for i in array)
	isSorted = True
	prev = generator.next()
	for item in generator:
		if(prev < item):
			prev = item
		else:
			isSorted = False
			break
	return isSorted

try:
	array = list(map(int,raw_input('Vvedite znachenia cherez probel: ').split(' ')))
except:
	print("Error vvoda")
else:
	print isSortedArray(array)
	
