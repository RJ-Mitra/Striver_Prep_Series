#given array of elements, find the majority element
#majority element is the one that occurs in the arr > n/2 times (i.e. more than half of the arr has it)

#problem guarantees there exists atleast 1 majority element (whose occurence is greater than n/2)

input_list = [2,2,1,1,1,2,2]
#expected = 2

#Approach 1: Get counts using map. If element count > n/2, marks as majority element.

#Optimal Approach:
#Moore's Voting Algo

#Logic:
# Wherever the curr_count becomes 0, that part of the arr is where there is no majority element.
# E.g. as per given arr, curr_count becomes 0 after 2,2,1,1. We can see there is not majority here.
# Hence we disregard that part of our algo and start our majprity counts from the right sub-arr

def find_majority(arr):
    curr_majority = -1
    curr_count = 0 #no majority at start
    for i in input_list:
        if curr_count == 0: #if no majority boundary is reached, we take curr element as new majority and discard everything to left
            curr_majority = i
            curr_count+=1
        elif i == curr_majority:
            curr_count+=1
        else: #if we find a new element which is not = curr_majority elem, we decrease count by 1 (till it reaches 0)
            curr_count-=1
    return curr_majority

print(find_majority(input_list))
