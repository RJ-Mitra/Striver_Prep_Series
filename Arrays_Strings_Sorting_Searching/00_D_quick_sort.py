unsorted = [4,9,2,96,14,1,56,3]

#  We choose a random element as pivot (usually left, right or middle)
#  In quick sort, we find the partition where all elements to the left are
#  smaller than the pivot and all elements to the right are larger 
#  than the pivot. Once we find this pivot, we recurse to find pivot in the left
#  and right sub-arrays of the current pivot

#returns index of the pivot after partitioning
##### NOTE: With each partition, we bring all elements lesser than the pivot
## to the left of it, and all elements greater to the right. Then we put the
### pivot in its correct pos in middle, and quicksort the sub-arr to left & right of it
def partition(left, right):
    pivot = left #taking pivot as left
    while left<right: #while the ptrs don't cross over
        while unsorted[left] <= unsorted[pivot]: #we only swap if we find an element while is higher than the pivot on the left side
            left+=1
        while unsorted[right] > unsorted[pivot]: #and an element which is lower than pivot on the right side, as swapping will make sure the lower goes to left of pivot while higher goes to right of pivot
            right-=1
        if (left<right):
            unsorted[left],unsorted[right] = unsorted[right],unsorted[left] #swap
    unsorted[pivot],unsorted[right] = unsorted[right],unsorted[pivot] #when the pointers cross over, the index of the right pointer is the partition index. We place the pivot value at this index and return it to call qsort on both sides of this index
    return right

def quickSort(left, right):
    if left<right: #makes sure we have atleast 2 elements in the arr
        partitioned = partition(left,right) #finds partition index
        quickSort(left, partitioned-1) #calls qsort on sub-arrays on both side of partition index
        quickSort(partitioned+1, right)

print(unsorted)
quickSort(0,len(unsorted)-1)
print(unsorted)

    