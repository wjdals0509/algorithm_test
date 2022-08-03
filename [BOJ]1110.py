#int ver.
N = int(input()) # 68
nN = N
cnt = 0
while True:
    a = nN // 10 # 6
    b = nN % 10 # 8
    c = (a+b) % 10 # 6 + 8 = 1"4"
    nN = (b * 10) + c # 80 + 4 = 84
    cnt += 1 #사이클 수 +1
    if(nN == N): #nN에서 입력된 N과 똑같은 숫자(68)가 나오면 멈춤
        break
print(cnt) 

"""
#str ver.
N = input()
nN = N
cnt = 0
while 1:
    if len(nN) == 1: #문자열의 길이가 1(즉, N이 10보다 작을 때)
        nN="0"+nN
    plus = str(int(nN[0]) + int(nN[1])) # nN = [2, 6] / 2 + 6 = "8"
    nN = nN[-1] + plus[-1] # "6" + "8" = "68"
    cnt += 1 #사이클 수
    if nN == N:
        print(cnt)
        break
"""