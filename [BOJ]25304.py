x=int(input())
n=int(input())
price=[]
for _ in range(n):
    a,b=map(int, input().split())
    price.append(a*b) #입력 받은 값을 리스트에 삽입
if x==sum(price):
    print("Yes")
else:
    print("No")
