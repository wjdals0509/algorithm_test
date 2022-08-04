c=int(input()) #테스트 케이스 개수
for i in range(c):
    x=list(map(int, input().split())) #학생수, 학생수 만큼의 점수
    result=sum(x[1:])/x[0] #평균점수(점수/학생수)
    student=0 #평균 이상인 학생 수 초기화
    for j in x[1:]:
        if j>result: #점수가 평균보다 높을 때
            student+=1 #누적 평균 이상 학생 수
    rate=student/x[0]*100 #평균 이상인 학생의 비율
    print(f'{rate:.3f}%') # 소수점 셋째 자리까지 출력