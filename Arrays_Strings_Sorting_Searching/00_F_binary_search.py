sorted_list = [1, 2, 3, 4, 9, 14, 56, 96]
n = 96

def binarySearch(sorted_list, l, r, n):
    if l<=r:
        mid = (l+r)//2
        if sorted_list[mid] == n:
            return True
        if n<sorted_list[mid]:
            return binarySearch(sorted_list,l,mid-1,n)
        else:
            return binarySearch(sorted_list,mid+1,r,n)
    else:
        return False

def binarySearch_iter(sorted_list,n):
    low = 0
    hi = len(sorted_list)-1
    while low<=hi:
        mid = (low+hi)//2
        if sorted_list[mid] == n:
            return True
        if n < sorted_list[mid]:
            hi = mid-1
        else:
            low = mid+1
    return False


print(binarySearch_iter(sorted_list,n))

