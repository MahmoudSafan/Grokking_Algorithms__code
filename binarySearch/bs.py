# O(log(n)) logarithmic time

def binarySearch(myList,item): 
	Min = 0
	Max = len(myList)-1
	while Max - Min >= 0:
		Mid = (Min+Max)//2
		print(Mid)

		if myList[Mid] == item:
			return Mid

		elif myList[Mid] > item:
			Max = Mid-1

		elif myList[Mid] < item:
			Min = Mid+1

		else:
			return None


myList = [1,2,5,7,8,9,10,12,56,455]

print(binarySearch(myList,5))