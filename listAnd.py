#有两个长度为N的有序序列A和B，
#在A和B中各任取一个数可以得到N^2个和，
#求这N^2个和中最小的N个。
l=[14,15,16,17,20]
s=[14,15,17,20,43]
t=[]
for i in l:
    a=[]
    for j in s:
        a.append(i+j)
    t.append(a)
n=[]
d=0
k=1
while d<len(l):
    d=d+k
    k=k+1

for e in range(0,k-2):
    for f in range(0,k-2-e):
        print t[e][f]
p=[]        
for m in range(0,k-1):
    p.append(t[m][k-1-m])

q=len(l)-d+k-1
if q>len(p):
    q=len(p)
s=[]
for i in p:
    s.append(i)
    if len(s)>q:
        max=0
        for j in range(0,len(s)):
            if s[j]>s[max]:
                max=j
        del(s[max])
for r in s:
    print r