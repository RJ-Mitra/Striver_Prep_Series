#Two problem types

#1.
#Elements sorted and value of last element in prev row < val of 1st element in next row

leet = [[1,3,5,7],
        [10,11,16,20],
        [23,30,34,50]]

leet_target = 34

def helper_b_search(arr,left,right,x):
    #print(arr)
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == x:
            return True
        elif x < arr[mid]:
            right = mid-1
        else:
            left = mid+1
    return False

# print(helper_b_search(leet[0],0,3,6))

#approach 1: (sub-optimal)
def search_leet(arr,x):
    left = 0
    right = len(arr)-1
    row = 0
    col = len(arr)-1
    if x<= arr[row][col]: #if in 1st row itself
        return helper_b_search(arr[0],row,col,x)
    else:
        while row<len(arr)-1:
            if x > arr[row][col] and x<=arr[row+1][col]:
                return helper_b_search(arr[row+1],left,right,x)
            else:
                row+=1
    return False

print("leet1: ", search_leet(leet,leet_target))

#approach 2: (Optimal)
#Calculate matrix like a single full array
#Calculate cumulative row and col using formula:
#m = len(arr[0])
#row = mid/m
#col = mid%m

def search_leet_opt(arr,x):
    n = len(arr)
    m = len(arr[0])
    left = 0
    right = (m*n)-1 #since indexing starts from 0 till len -1
    while left<=right:
        mid = (left+(right-left)//2)
        if arr[mid//m][mid%m] == x:
            return True
        elif x>arr[mid//m][mid%m]:
            left = mid+1
        else:
            right=mid-1
    return False

print("Leet optimised: ", search_leet_opt(leet,leet_target))

#2
#Elements sorted in both row and column level, but last element of prev is not < 1st element of next row

gfg = [[10,20,30,40],
       [15,25,35,45],
       [27,29,37,48],
       [32,33,39,50]]

gfg_target = 37

#Approach: Start from top right and move down or left depending on element value compared to target
def search_gfg(arr,x):
    i = 0
    j = len(arr[0])-1
    while i<=len(arr[0])-1 and j>=0:
        if arr[i][j] == x:
            return True
        elif x > arr[i][j]:
            i+=1
        else:
            j-=1
    return False

print(search_gfg(gfg,gfg_target))


