#Reverse pairs
#Similar to inverse_count (08) except valid pairs are i<j and arr[i] > 2* arr[j]

arr = [2,4,3,5,1]

#expected = 3 (4,1),(3,1),(5,1),

#Approach: Modified merge sort

def merge(arr,l,m,r):
    count = 0 #finding pair count here
    j = m+1
    for i in range(l,m+1): #for each element in left arr (arr[i])
        while j<=r and arr[i] > (2*arr[j]): #logic: for every element that satisfies the condition, we move j to the right. When j reaches end, all elements for i and to right of current i can form a valid pair with j
            j+=1 #if arr[i] can form a pair with arr[j], since list is sorted, it can form a pair with all elements to the right of j
        count+=(j-(m+1))
    #find pair ends here
    temp = arr[:] #merge step starts
    i = l
    j = m+1
    k = l
    while i<=m and j<=r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1
    while i<=m:
        temp[k] = arr[i]
        k+=1
        i+=1
    while j<=r:
        temp[k] = arr[j]
        k+=1
        j+=1
    k = l
    while k<=r:
        arr[k] = temp[k]
        k+=1
    return count



def mergeSort(arr,l,r):
    count = 0
    if l>=r: #to not divide when only 1 element is in arr
        return 0
    else:
        mid = (l+r)//2
        count+=mergeSort(arr,l,mid)
        count+=mergeSort(arr,mid+1,r)
        count+=merge(arr,l,mid,r)
    return count


print(arr)
print("Res: ", mergeSort(arr,0,len(arr)-1))
print(arr)
