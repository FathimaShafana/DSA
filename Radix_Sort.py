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
