unsorted = [4,9,2,96,14,1,56,3]

#Left part of array is considered sorted. We pick an element and place it in it's correct position in the sorted part of the array
#diff with selection sort: In selection sort, we pick the smallest element in each iteration

def insertionSort(unsorted):
    temp = -1
    for i in range(1,len(unsorted)): #considering 1st element as sorted and starting comparison from 2nd (left part of array is sorted)
        temp = unsorted[i]  #storing current var that is being compared in temp
        j = i-1 #pointer to compare and shift values to right if they are greater than current
        while j>=0 and unsorted[j]>temp: #while j is within the bounds of array (>=0) and the curr element is greater than temp, we shift it to the right
            unsorted[j+1] = unsorted[j]
            j-=1 #move j to the element left of curr and compare again
        unsorted[j+1] = temp #once temp is at it's left most position, we insert it in it's place (j+1 since we do j-- in prev step)
    return unsorted

print(unsorted)
print(insertionSort(unsorted))