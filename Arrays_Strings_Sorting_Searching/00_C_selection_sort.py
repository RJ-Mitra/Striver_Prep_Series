#Selection sort selects the lowest element in each iteration and drops it in it's current position

unsorted = [4,9,2,96,14,1,56,3]

#diff with selection sort: In selection sort, we pick the smallest element in each iteration

def selectionSort(unsorted):
    left = 0 #starting from left of the arr, we find the smallest element in the arr
    while left<len(unsorted):
        i = left
        smallest = i #storing index of smallest element encountered till now
        while i<len(unsorted):
            if unsorted[i] < unsorted[smallest]:
                smallest = i #we record smallest element till now
            i+=1
        if smallest != left: #if a new smaller element is encountered, we swap it with the leftmost value.
            unsorted[smallest],unsorted[left] = unsorted[left],unsorted[smallest]
        left+=1 #now, left most element has the smallest value, i.e. sorted. So we increment left by 1 and find another smallest elem in rest of the arr from left+1 to end of arr
    return unsorted

print(unsorted)
print(selectionSort(unsorted))