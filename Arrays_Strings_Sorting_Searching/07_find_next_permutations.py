#find next permutation
# E.g. Given -> 213, next permutation is 231. 
# EDGE case: If given is the last in the list, return the 1st permutation i.e given -> 321, return 123

#nput = 13542 #to 14235
input = 54321 #edge case

#converting to list
input_list = list(str(input))
print(input)

#find break index
break_idx = -1
#starting from end element, find the 1st instance where list[a] < list[a+1]
for i in reversed(range(len(input_list)-1)):
    if input_list[i] < input_list[i+1]:
        break_idx = i
        break

print(break_idx)
#EDGE CASE:
#if last permutation is supplied as input, i.e. breakpoint < 0
if break_idx < 0:
    print(''.join(list(reversed(input_list))))
else:
    #again iterating from right till the break point, find the index having value greater than value at break_idx
    lesser_val_idx = -1
    for i in reversed(range(len(input_list))):
        if input_list[i] > input_list[break_idx]:
            lesser_val_idx = i
            break

    #swap the values at the two indexes
    input_list[break_idx], input_list[lesser_val_idx] = input_list[lesser_val_idx], input_list[break_idx]

    #reverse all the values present after break point index
    values_before_break_idx = [input_list[i] for i in range(break_idx+1)]
    reversed_values_after_break_idx = list(reversed([input_list[i] for i in range(break_idx+1, len(input_list))]))

    print(values_before_break_idx)
    print(reversed_values_after_break_idx)

    #add the values
    next_permut = values_before_break_idx + reversed_values_after_break_idx
    print(''.join(next_permut))
