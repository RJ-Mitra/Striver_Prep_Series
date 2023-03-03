unsorted = [4,9,2,96,14,1,56,3]

#divide and conquer

def merge(unsorted,l,mid,h):
    temp_list = unsorted[:]
    i = l
    j = mid+1
    k = l
    while i<=mid and j<=h: #sorting and merging
        if unsorted[i] < unsorted[j]:
            temp_list[k] = unsorted[i]
            i+=1
        else:
            temp_list[k] = unsorted[j]
            j+=1
        k+=1
    while i<=mid: #merging remaining elements in either one of the two lists
        temp_list[k] = unsorted[i]
        k+=1
        i+=1
    while j<=h:
        temp_list[k] = unsorted[j]
        j+=1
        k+=1
    k = l #copying temp list elements to main list
    while k<=h:
        unsorted[k] = temp_list[k]
        k+=1


def mergeSort(unsorted,l,h):
    if l<h: #merge only id the sublist/list has atleast 2 elements. If it has 1 element, it's already sorted
        mid = (l+h)//2 #divide into 2 sub lists
        mergeSort(unsorted,l,mid) #calling merge on both sub lists
        mergeSort(unsorted,mid+1,h)
        merge(unsorted,l,mid,h) #merging the sub-lists

print(unsorted)
mergeSort(unsorted,0,len(unsorted)-1)
print(unsorted)
    