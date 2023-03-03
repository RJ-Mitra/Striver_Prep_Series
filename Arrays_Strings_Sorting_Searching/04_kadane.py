#find largest sub-array sum

l1 = [-2,1,-3,4,-1,2,1,-5,4]

curr_sum = float("-inf")
max_sum = float("-inf")

for i in range(len(l1)):
    curr_sum = max(curr_sum+l1[i],l1[i])
    max_sum = max(curr_sum, max_sum)

print(max_sum)
