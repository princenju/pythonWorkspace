#��ƽ��ʱ�临�Ӷ�O(n)���㷨����Ϊ���ǿ�����O(n)��ʱ�����ҵ�δ�������������kС������ֵ��
#Ȼ���ٱ���һ�����飬
#��ֵС�ڵ��ڵ�kС��ȫ�����
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