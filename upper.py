#昨天面试遇到一题，
#要求将输入的大写字母转成对应小写的后5个，
#如A转换后为f；如果转换后大于z则从a重新计，
#即多出1就转成a,
#多出2就转成b以此类推。
a=['s','t','a','c','k','z']
print ord('a')
print ord('A')
print ord('Z')
for item in range(0,len(a)):
    a[item]=chr((ord(a[item])+5-32-65)%26+65)
print a