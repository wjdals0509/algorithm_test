n=int(input()) #과목수
score=list(map(int,input().split())) #과목점수
m=max(score) #과목점수 중 최대값
for i in range(n):
    score[i]=score[i]/m*100 #조작된 점수
print(sum(score)/n) #새로운 평균(조작된점수/과목수)
    
    

