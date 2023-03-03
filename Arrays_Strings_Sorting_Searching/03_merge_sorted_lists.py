#Given two sorted lists, merge them (preferably in place)

from math import ceil


list1 = [3,27,38,45]
list2 = [9,10,82]

3,9,38,45
27,10,82

3,9,38,45
10,27,82

3,9,10,45
38,27,82

3,9,10,45
27,38,82

3,9,10,27
45,38,82

3,9,10,27
38,45,82


#Brute force: Use extra space, then insert them back in sorted order in each list (can use two pointers)

def swap(a,b):
    a,b = b,a

#optimised1:
#Compare each element between two lists
l1_idx = 0
l2_idx = 0
while l1_idx < len(list1):
    if list1[l1_idx] <= list2[l2_idx]: #if still sorted, move to next element in 1st list
        l1_idx+=1
    else:
        list1[l1_idx],list2[l2_idx] = list2[l2_idx], list1[l1_idx] #if any elem is not sorted, always swap with 1st element of 2nd list, then sort the 2nd list
        list2.sort()

print(list1)
print(list2)
            


#optimised2:
#similar to shell sort

#create group size that will be halved for each iteration till it is 1

def nextGap(gap):
    if gap <= 1:
        return 0
    return gap//2 + gap%2


def merge(l1, l2, n, m):
    gap = n+m
    gap = nextGap(gap)
    while gap >= 1:
        i = 0
        while i+gap < n:
            if(l1[i] > l1[i+gap]):
                l1[i],l1[i+gap] = l1[i+gap],l1[i]
            i+=1
        j=gap-n if gap>n else 0
        while i<n and j<m:
            if (l1[i] > l2[j]):
                l1[i],l2[j] = l1[j],l2[i]
            i+=1
            j+=1
        if j<m:
            j=0
            while j+gap < m:
                if (l2[j] > l2[j+gap]):
                    l2[j],l2[j+gap] = l2[j+gap],l2[j]
                j+=1
        gap=nextGap(gap)


l1 = [3,27,38,45]
l2 = [9,10,82]
n = len(l1)
m = len(l2)

merge(l1,l2,n,m)

print(l1)
print(l2)




