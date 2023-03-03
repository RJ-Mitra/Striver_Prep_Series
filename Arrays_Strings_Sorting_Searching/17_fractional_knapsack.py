#given item values and weights as well as a knapsack capacity, fit max value into that knapsack
#Fractional - can break items based on weights

values = [60,100,120]
weights = [10,20,30]
capacity = 50

#Expected: 240

class Item:
    def __init__(self,val,wt):
        self.val=val
        self.wt=wt

item_list : Item = []

for i in range(len(values)):
    item_list.append(Item(values[i],weights[i]))

sorted_list : Item = []

#sort items in order of max value per weight (DESC of val//wt)
sorted_list = sorted(item_list, key = lambda x: x.val//x.wt > 1) #swaps if res > 1, else doesn't swap

c = capacity
res_val = 0
i=0

while c>0:
    if i>=len(sorted_list):
        break
    item = sorted_list[i] #extra: check to make sure i does not go out of index (less elements than capacity)
    if item.wt <= c:
        res_val+=item.val
    else:
        res_val = res_val + ((c* item.val)//item.wt)
    c-=item.wt
    i+=1

print(res_val)

