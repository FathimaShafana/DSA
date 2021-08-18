# To obtain the array in ascending order
def insertionSortAsc(array):
 
    
    for i in range(2, len(array)):
 
        key = array[i]
 
        j = i-1
        while j >= 0 and key < array[j] :
                array[j + 1] = array[j]
                j = j-1
        array[j + 1] = key
 
# To obtain the array in descending order 
def insertionSortDesc(array):
 
    
    for i in range(2, len(array)):
 
        key = array[i]
 
        j = i-1
        while j >= 0 and key > array[j] :
                array[j + 1] = array[j]
                j = j- 1
        array[j + 1] = key

array = [25, 31, 56, 11, 10, 5]
insertionSortAsc(array)
print("In Ascending Order")
for i in range(len(array)):
    print (array[i])
 
print("\nIn Descending Order")
insertionSortDesc(array)
for i in range(len(array)):
    print (array[i])
