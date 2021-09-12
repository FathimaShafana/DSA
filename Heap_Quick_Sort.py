#Package imports
import time   
import numpy as np
import matplotlib.pyplot as plot  

## Implement Heap Sort

def Left(i):
    return 2 * i

def Right(i):
    return (2 * i) + 1
  
#Optional
def Parent(i):
    return i // 2
  
#Function Max_heapify
def max_Heapify (A, i):
    size = len(A)
    largest = i  
    l = Left(i)
    r = Right(i)
    
    if l <= size and A[i] < A[l]:
        largest = l
    else:
        largest = i
        
    if r <= size and A[i] < A[r]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A [largest], A[i]
        max_Heapify (A, largest)

#Build Max Heap function        
def build_Max_Heap (A):
    #Array.heapSize = len(Array)
    size = len(A)
    for i in range (size//2, 1, -1):
        max_Heapify (A, i)

        
#Heap Sort function  
def heap_Sort(A):
    size =len(A)
    build_Max_Heap(A)
    
    for i in range (size, 2, -1):
        A[1] , A[i] = A[i], A[1]
        max_Heapify (A, 1)

#### QUICK SORT
#Function Partition
def partition (A,p,r):
    x = A[r]
    i = p-1
    
    for j in range (p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1 
  
#Function Quick Sort
def quickSort(A,p,r):
    if p<r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
        
#Testing the functions heapsort and quick sort
#Test Print
Array_Test1 = [2,5,8,4,3,11, 42]
n = len(Array_Test1)
quickSort(Array_Test1, 0, n -1)
print ("Sorted array using Quick Sort is" , Array_Test1)

Array_Test2 = [2,5,8,4,3,11, 42]
heapSort(Array_Test2)
n = len(Array_Test2)
print("Sorted Array using HeapSort is", Array_Test2)

#Compare complexity using real time calculation
elements1 = list()    #To store the number of elements compared for quick sort
elements2 = list()    #To store the number of elements compared for heap sort
times_quick = list()  #To store the time taken by quick sort for each number of elements
times_heap = list()   #To store the time taken by heap sort for each number of elements


for i in range(1, 7): 
    
    A1 = np.random.randint(-1000, 1000, size=pow(10, i)) 
    n1 = len(A1)
    
    A2 = np.random.randint(-1000, 1000, size=pow(10, i)) 
    n2 = len(A2)
    
    start_time_quick = time.process_time()
    quickSort(A1, 0, n1-1)  
    end_time_quick = time.process_time()   
    total_time_quick = end_time_quick - start_time_quick  

#   print("Number of elements = ",len(A1), "Time spent" , + total_time_quick, "sec")

    elements1.append(len(A1))
    times_quick.append(total_time_quick)
    
    
    start_time_heap = time.process_time()
    heapSort(A2)  
    end_time_heap = time.process_time()   
    total_time_heap = end_time_heap - start_time_heap  

#   print("Number of elements = ",len(A2),"Time spent" , + total_time_heap, "sec")

    elements2.append(len(A2))
    times_heap.append(total_time_heap)


plot.xlabel('Number of values in the array')
plot.xscale("log", base=10)
plot.ylabel('Time spent by the sorting algorithm')
plot.plot(elements1, times_quick, color='red', label='Complexity quick sort')
plot.plot(elements2, times_heap, color='blue', label='Complexity heap sort')
plot.grid()
plot.legend()
plot.show()
