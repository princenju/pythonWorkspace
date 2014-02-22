#求一个集合的所有真子集
a=set("subset")
b=list(a)
print b
for i in range(0,2**len(b)):
    l=[]
    for j in range(0, len(b)):
        if i%2==1:
            l.append(b[j])
            i=(i-1)/2
        else:
            i=i/2
    print l
    