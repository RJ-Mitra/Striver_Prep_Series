# Same logic as majority 1, except we can have multiple majorities in the list
# here, there might be at most 2 majorities in the list
# i.e. count of each majority should be > n/3

#Modified version of Boyer Moore Voting Algo

arr = [1,1,1,3,3,2,2,2]

#Expected: [1,2]

def get_majority_elements(arr):
    curr_maj_1 = -1 #two vars to track curr majority elements
    curr_maj_2 = -1
    curr_count_1 = 0
    curr_count_2 = 0
    for i in arr:
        if i == curr_maj_1: #if same encountered, increment count
            curr_count_1+=1
        elif i == curr_maj_2:
            curr_count_2+=1
        elif curr_count_1 == 0: #if 0 reached, then this element is not majority now.
            curr_maj_1 = i #take new element as maj
            curr_count_1 = 1 #change curr maj count to 1
        elif curr_count_2 == 0:
            curr_maj_2 = i
            curr_count_2 = 1
        else: #if something encountered that's not either elem1 or elem2, we decrease count of both by 1
            curr_count_1-=1
            curr_count_2-=1
    res = []
    len_arr = len(arr)
    count1 = 0
    count2 = 0
    for i in arr:
        if i == curr_maj_1:
            count1+=1
        elif i == curr_maj_2:
            count2+=1
    if count1> len_arr//3:
        res.append(curr_maj_1)
    if count2> len_arr//3:
        res.append(curr_maj_2)
    return res

print(get_majority_elements(arr))


