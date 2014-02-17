#有平均时间复杂度O(n)的算法，因为我们可以在O(n)的时间内找到未排序数组里面第k小的数的值，
#然后再遍历一下数组，
#把值小于等于第k小的全都输出
l=[15,16,20,14,2,17]
k=input("k=")
if k>len(l):
    k=len(l)
s=[]
for i in l:
    s.append(i)
    if len(s)>k:
        max=0
        for j in range(0,len(s)):
            if s[j]>s[max]:
                max=j
        del(s[max])
print s