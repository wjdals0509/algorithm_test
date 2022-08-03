A=int(input())
B=int(input())
C=int(input())
result=A*B*C
n = list(map(int,str(result))) # 각 자리수를 리스트로 변환
for i in range(10):
    x = n.count(i)
    print(x)


