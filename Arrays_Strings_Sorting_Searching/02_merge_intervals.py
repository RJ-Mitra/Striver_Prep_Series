class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self) -> str:
        return ("Start: "+str(self.start)+" End: "+str(self.end))

i1 = Interval(1,3)
i2 = Interval(2,6)
i3 = Interval(8,10)
i4 = Interval(15,18)

#print(i1)

ilist = [i1,i2,i4,i3]

# for i in ilist:
#     print(i)

sorted_ilist = sorted(ilist, key=lambda x: x.start) #sorting

res = []
start = sorted_ilist[0].start
end = sorted_ilist[0].end

for i in sorted_ilist:
    curr = i
    if curr.start <= end: #if start time of current slot falls before end of prev slot
        end = max(end, curr.end) #we merge the curr into the prev slot
    else:
        new_insert = Interval(start,end) #else, we insert next one as a separate slot
        res.append(new_insert)
        start = curr.start
        end = curr.end
res.append(Interval(start,end)) #entering the slot into results after merge

for i in res:
    print(i)

# for i in sorted_ilist:
#     print(i)