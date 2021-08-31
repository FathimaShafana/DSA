#Package imports
import time   
import numpy as np
import matplotlib.pyplot as plot 

#To find maximum sub array
def maxSubArray(A, low, high):
    #For one element (Best Case)
    if low == high:     
        return low, high, A[low]
    #else:
    mid = (low + high) // 2    #Floor division
#         (left_low,left_high,left_sum) = maxSubArray (A,low,mid)
#         (right_low,right_high,right_sum) = maxSubArray(A, mid+1, high)
#         (cross_low,cross_high, cross_sum) = max_crossing_subarray(A,low,mid,high)
        
#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return (left_low,left_high,left_sum)
#         elif right_sum >= left_sum and right_sum >=cross_sum:
#             return (right_low,right_high,right_sum) 
#         else:
#             return (cross_low,cross_high, cross_sum)
        
    return max(maxSubArray(A, low, mid),                
               maxSubArray(A, mid + 1, high),           
               max_crossing_subarray(A, low, mid, high))  

#To find maximum crossing sub array
def max_crossing_subarray (A,low,mid,high ):
    left_sum = -10000
    sum = 0
    for i in range (mid,low-1,-1):
        sum = sum + A[i]
        
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    right_sum = -10000
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]

        if sum > right_sum:
            right_sum = sum
            max_right = j
            
        return max(left_sum + right_sum, max_left, max_right) 
#       return left_sum + right_sum, max_left, max_right

#Actual Time Spent vs Theoretical Complexity
elements = list()   
times = list()      
complexity = list ()

#For theoretical complexity, let c = 1/500000
c = 1 / 500000
for i in range(1, 7): 
    
    A = np.random.randint(-1000, 1000, size=pow(10, i))
    
    n = len(A)
    y_nlogn = c*(n*np.log(n))
    #print(A)
    start_time = time.process_time()  # Sstart time before run
    max_sum = MaxSubArray(A, 0, n - 1)  # Calling function
    print("Maximum contiguous sum is ", max_sum)
    end_time = time.process_time()    # Start time after execution
    total_time = end_time - start_time  # Total time taken 

    print(len(A), "Elements of random integer was executed in ", + total_time, "sec")

    elements.append(len(A))
    times.append(total_time)
    complexity.append(y_nlogn)


plot.xlabel('Number of values in the array')
plot.xscale("log", base=10)
plot.ylabel('Time spent by the algorithm')
plot.plot(elements, times, color='red', label='Actual time spent by algorithm')
plot.plot(elements, complexity, color='blue', label='Theoretical complexity of algorithm')
plot.grid()
plot.legend()
plot.show()
