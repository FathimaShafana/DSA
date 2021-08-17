def mergeSort(A,p,r):
    if p < r:
        q = (p + r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        
        merge(A,p,q,r)

def merge(A,p,q,r):
    n1= q-p+1
    n2=r-q
    L=A[n1]
    R=A[n2]

    for i in (1,n1):
        L[i] = A[p+i-1]

    for j in (1,n2):
        R[j]=A(q+j)

        i=j=1
        for k in (p,r):
            if L[i] <= R[j]:
                A[k] = L[i]
                i=i+1

            elif A[k] == R[j]:
                j=j+1

        
A = [25, 31, 56, 11, 10, 5] 
p=1
r=len(A)
mergeSort(A,p,r)
merge(A,p,q,r)
printlist(A)
