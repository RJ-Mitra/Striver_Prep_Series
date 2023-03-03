unsorted = [4,9,2,96,14,1,56,3]

def bubbleSort(unsorted):
    flag = True
    while flag:
        flag = False #flag to terminate if all elements are already sorted before all iterations are over
        end = 1 #in each iteration, the largest element bubbles down to the end, so in next iteration we can consider till end - 1
        for i in range(0,len(unsorted)-end):
            if unsorted[i] > unsorted[i+1]:
                flag = True
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
        end-=1
    return unsorted


print(unsorted)
print(bubbleSort(unsorted))
            

