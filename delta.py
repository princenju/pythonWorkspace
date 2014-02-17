n=int(input("n="))
myList = [([0]*(2*n-1)) for i in range(n)]
myList[0][n-1]=1
for i in range(1,n):
    for j in range(0,2*n-1):
        if j-1<0:
            myList[i][j]=0+myList[i-1][j+1]
        elif j+1>2*n-2:
            myList[i][j]=myList[i-1][j-1]+0
        else:
            myList[i][j]=myList[i-1][j-1]+myList[i-1][j+1]
for k in myList:
    print k