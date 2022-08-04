T=int(input()) #테스트 케이스 개수 입력
for i in range(T): #테스트 케이스 만큼 반복
    result=list(input()) #OX퀴즈 결과 입력
    score=0 #점수 초기화
    sum_score=0 #새로운 OX리스트를 입력 받으면 점수 합계 초기화
    for i in range(len(result)): #OX퀴즈 개수 만큼 반복
        if result[i] == "O": #OX퀴즈 결과가 O일때
            score+=1 #O가 연속되면 점수가 1씩 커짐
            sum_score+=score
        else:
            score=0
    print(sum_score)
        
        