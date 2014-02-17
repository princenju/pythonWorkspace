l1=[1,4,2]
l2=l1[::-1]
l3=[]
for i in range(0,len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
print l3