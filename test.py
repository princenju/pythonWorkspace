def hello():
    list =[1,2,5,9,0,4]
    max=0
    for i in range(0,len(list)):
        for j in range(i,len(list)):
            result=min(list[i],list[j])*(j-i)
            if result>max:
                max=result
                print list[i]
                print list[j]
                print max;
if __name__=='__main__':
    hello()