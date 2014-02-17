count=[1,2,0,1,3,4]
mylist = [0 for n in range(len(count))]
for i in count:
    mylist[i]=mylist[i]+1
print mylist