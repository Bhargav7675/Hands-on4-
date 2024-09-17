def merge(arr):
    '''
    Given K sorted arrays of size N each
    The sorted array is compressed in one list arr,
    for example, arr=[[1,3,5,7], [2,4,6,8], [0,9,10,11]]
    '''
    k=len(arr)
    n=len(arr[0])
    pointers=[0]*k
    sortedArr=[]
    for _ in range(k*n):
        min_value=float('inf')
        min_index=-1
        for i in range(k):
            if pointers[i]<n and arr[i][pointers[i]]<min_value:
                min_value=arr[i][pointers[i]]
                min_index=i
        sortedArr.append(min_value)
        pointers[min_index]+=1
    return sortedArr

arrays1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
arrays2 = [[1, 3, 7], [2, 4, 8], [9, 10, 11]]
print(merge(arrays1))
print(merge(arrays2))