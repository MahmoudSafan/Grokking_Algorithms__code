def findSmallest(arr):
    minEl = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < minEl:
            minEl  = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        ind = findSmallest(arr)
        newArr.append(arr.pop(ind))
    return newArr

arr = [1000,2000,-20,100,50,60,99]

print(selection_sort(arr))


