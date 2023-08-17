T = int(input())
answer = 0
for tc in range(1, T+1):
    a = list(map(int, input().split()))
    for i in a:
        if i%2 != 0:
            answer += i
    print("#{} {}".format(tc, answer))