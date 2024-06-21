def removeDuplicates(array, value):
    for i in range(len(array)):
        if array[i] == value:
            array[i] = array[i + 1]
    
    return array

array = [1, 1 ,2,3,1]
# res = removeDuplicates( [1,2,3,4,3,5], 3)



def dedup(arr, target):
    j = 0
    for i in range(len(arr)):
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1
    return arr[0:j]       

print(dedup([1,3,3,5],3))

