#Given a mxn grid, find the number of paths from start to end if you can only move right and down

m = 2 #rows
n = 3 #cols

#expected = 3

def find_paths(m,n):
    i = 0 #starting indexes
    j = 0
    return find_paths_recursive(i,j,m,n)

def find_paths_recursive(i,j,m,n):
    if i == m-1 and j == n-1:
        return 1 #returns 1 if a path end if found. All such ends are added at the end to get count of all paths
    if i>=m or j>=n:
        return 0
    return find_paths_recursive(i+1,j,m,n) + find_paths_recursive(i,j+1,m,n)

print(find_paths(m,n))

#Optimised: Using hash table to store state (DP) to avoid recalculations

dp = [[-1 for j in range(n)] for i in range(m) ]
#print(dp)

def find_paths_optimised(i,j,m,n):
    if i == m-1 and j == n-1:
        return 1
    if i>=m or j>=n:
        return 0
    if dp[i][j] == -1:
        dp[i][j] = find_paths_optimised(i+1,j,m,n) + find_paths_optimised(i,j+1,m,n)
    return dp[i][j]

print("optimised: ", find_paths_optimised(0,0,m,n))



