import math

def insertionSort(A):
 
    # For each element in array 
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def bucketSort(A):
    B=[]
    bucket = len(A)
    
    #MEmpty list
    for i in range(bucket):
        B.append([])
    
    #Get Index of bucket  
    for i in A:
        index_b = int(bucket * i)
        B[index_b].append(i)
    
    #Insertion Sort
    for i in range(1,bucket):
        insertionSort(B[i])
    print (B)
    
    
#Test Array
A = [0.78,0.25,0.41,0.98,0.11,0.42,0.32,0.17,0.36,0.58]

print('The input array:')
print(A)
print('Sorted Array:')
bucketSort(A)
