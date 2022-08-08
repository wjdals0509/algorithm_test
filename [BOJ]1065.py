def hansu(n):
    cnt=0
    for i in range(1,n+1):
        x=list(map(int,str(i))) #str로 형변환 후 list화 ex) x=[1,3,5]
        if (i<100): #100이하는 무조건 한수(매우 중요)
            cnt+=1
        elif (x[2]-x[1] == x[1]-x[0]): #자릿수끼리 등차가 일정할 때(등차수열일 때)
            cnt+=1
    return cnt
n=int(input())
print(hansu(n))