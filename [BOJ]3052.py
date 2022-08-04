m = []
for i in range(10):
    n=int(input()) #정수 입력 받음
    m.append(n%42) #n을 42로 나눈 나머지들을 리스트m에 요소로 삽입(append)
print(len(set(m))) #set으로 중복요소 제거, len으로 원소 개수 출력 