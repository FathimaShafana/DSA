def countSort(A):
    n=len(A)
    maxA= int(max(A))
    minA= int(min(A))
    k = maxA - minA + 1

    #To store frequency
    C = [0] * (k)
    #To store sorted array
    B = [0] * (n)
 
    # Store count of each character
    for i in range(0, n):
        C[A[i]-minA] += 1
 
    for j in range(1, k):
        C[j] += C[j-1]
 
    # Output array
    for j in range(n-1, -1, -1):
        B[C[A[j] - minA] - 1] = A[j]
        C[A[j] - minA] -= 1
 
    for i in range(0, n):
        A[i] = B[i]
 
    return A

def radixSort(A):
    # FGet the number of digits in k
    k = max(A)
    d = 1
    while k / d > 0:
        countSort(A)
        d *= 10
                
#Test Array
array = [10, 15,33, 2500, 58, 21, 7,6, 1000]
radixSort(array)
for i in range(len(array)):
    print(array[i])

### Compare Radix Sort and Quick Sort
elements1 = list()   
elements2 = list()
times_radix = list()  
times_quick = list()


for i in range(1, 6): 
    
    A1 = np.random.randint(-1000, 1000, size=pow(10, i)) 
    n1 = len(A1)
    
    A2 = np.random.randint(-1000, 1000, size=pow(10, i)) 
    n2 = len(A2)
    
    start_time_radix = time.process_time()
    radixSort(A1)  
    end_time_radix = time.process_time()   
    total_time_radix = end_time_radix - start_time_radix  

    print("Number of elements = ",len(A1),"Time spent" , + total_time_radix, "sec")

    elements1.append(len(A1))
    times_radix.append(total_time_radix)
    
    
    start_time_quick = time.process_time()
    quickSort(A2, 0, n2-1)
    end_time_quick = time.process_time()   
    total_time_quick = end_time_quick - start_time_quick 

    print("Number of elements = ",len(A2),"Time spent" , + total_time_quick, "sec\n")

    elements2.append(len(A2))
    times_quick.append(total_time_quick)


plot.xlabel('Number of values in the array')
plot.xscale("log", base=10)
plot.ylabel('Time spent by the sorting algorithm')
plot.plot(elements1, times_radix, color='red', label='Complexity radix sort')
plot.plot(elements2, times_quick, color='blue', label='Complexity quick sort')
plot.grid()
plot.legend()
plot.show()
