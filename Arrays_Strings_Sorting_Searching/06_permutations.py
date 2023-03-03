#Given a number, find all possible permutations of that number

num = 123
#convert numbers of list

num_list = []

n = num
while n>0:
    rem = n%10
    n = n//10
    num_list.insert(0, rem)

results = []

def findAllPermutations(num_list, l, r):
    if l==r:
        results.append(num_list)
        print(num_list)
    else:
        for i in range(l,r):
            num_list[l],num_list[i] = num_list[i],num_list[l]
            findAllPermutations(num_list,l+1,r)
            num_list[l],num_list[i] = num_list[i],num_list[l]


(findAllPermutations(num_list,0,len(num_list)))
