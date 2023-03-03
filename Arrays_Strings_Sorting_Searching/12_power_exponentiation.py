#Implement pow(x,n) in optimised approach

#Approach:

#2^10
# -> 2^2^5 = (2 * 2) ^ 5 = 4^5
# -> 4^5 = 4 * 4^4
# -> 4*4^4 = 4*(4^2^2) = 4*(4*4)^2
# -> 16^2 = (16*16)^1 

def powerOf(x,n):
    res = 1
    if n == 0:
        return res
    nn = n
    while nn>0:
        if nn%2 == 0:
            x = x * x #pay attention to this x = x*x (basically x^x^n)
            nn = nn//2
        else:
            res = res * x #also pay attention to this res = res * x (basically res*x^n)
            nn = nn-1
    if  (n<0): #handling scenario where n might be negative
        res = 1.0/res #since x^-n = 1/x^n
    return res

print(powerOf(2,5))
print(powerOf(5,3))