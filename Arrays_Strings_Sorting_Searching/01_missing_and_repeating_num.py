list1 = [4,3,2,6,1,1]

#Numbers range from 1 to n. List has one missing element and 1 repeating element. Find them.

#Brute force: Use extra space (like a list with max number as size)
# to keep track of counts. Count of 2 is duplicate, count of 0 is missing elem.

#Optimal

#Formulas are S = n(n+1)/2 and S^2 = n(n+1)(2n+1)/6

#1. Get sum of all elements between least and highest elements in list (using formula above)
highest = max(list1)
sum_of_all, sq_sum_of_all = [0,0]
# sum_of_all = sum(range(1,highest+1))
# for i in range(1,highest+1):
#     sq_sum_of_all+=i**2

n = highest
sum_of_all = (n*(n+1))//2
sq_sum_of_all = (n*(n+1)*(2*n + 1))//6


#2. Get sum of all elements in given list as well as sq of all elements
list_sum, sq_list_sum = [0,0]
for i in list1:
    list_sum+=i
    sq_list_sum = sq_list_sum + (i*i)


#3. We know that,
#sum of all elements - (sum of elems in list + missing elem (i.e. x) - repeating elem (i.e. y)) = 0
# Hence, sum_of_all - list_sum  - x + y = 0
# Hence, sum_of_all - list_sum = x - y

x_minus_y = sum_of_all - list_sum

#Similarly, sq_sum_of_all (S^2) - (sq list - x^2 + y^2) = 0
#Hence, sq_sum_of_all - sq_list_sum = x^2 - y^2
#or sq_sum_of_all - sq_list_sum = (x+y)(x-y)

x_sq_minus_y_sq = sq_sum_of_all - sq_list_sum

#solving both equations
#(x+y)(x-y)/(x-y) = (x+y)
x_plus_y = x_sq_minus_y_sq//x_minus_y

#x+y + x-y //2 = 2x //2 = x
x = (x_plus_y + x_minus_y)//2

#y=x_plus_y - x
y = x_plus_y - x


print("Missing: "+ str(x))
print("Repeating: "+ str(y))




