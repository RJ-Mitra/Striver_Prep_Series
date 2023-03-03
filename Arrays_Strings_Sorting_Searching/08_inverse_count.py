#Given an array, find count of all elements satisfying the below condition:
#a[i] and a[j] form an inversion if a[i]>a[j] and i<j

#so, elements to left is greater than element to the right paired together form an inversion

arr = [8,4,2,1]
#Ans: 6
# [8,4],[8,2],[8,1],[4,2],[4,1],[2,1]

#Using a modified merge sort

def merge(arr, l, mid, r):
    inv_count = 0
    temp = arr[:]
    i=l
    j=mid+1
    k=l
    while i<=mid and j<=r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1
        else: #in this condition, a[i] > a[j] and i<j since left arr indexes will always be less than right arr indexes
            temp[k] = arr[j]
            inv_count = inv_count + (mid+1-i) #since both left and right arr are sorted, if a[i] > a[j], then every element to right of i will be greater than current arr[j] (since sorted). Hence, all elements to right of i (till mid+1, since j starts from mid+1 here) will form an inversion with current j 
            j+=1
        k+=1
    while i<=mid:
        temp[k] = arr[i]
        i+=1
        k+=1
    while j<=r:
        temp[k] = arr[j]
        j+=1
        k+=1
    k = l
    while k<=r:
        arr[k] = temp[k]
        k+=1
    return inv_count

def mergeSort(arr, l, r):
    inv_count = 0
    if l<r:
        mid = (l+r)//2
        inv_count+=mergeSort(arr,l,mid)
        inv_count+=mergeSort(arr,mid+1,r)
        inv_count+=merge(arr,l, mid, r)
    return inv_count

print(arr)
inv_count = mergeSort(arr,0,len(arr)-1)
print(arr)
print(inv_count)

