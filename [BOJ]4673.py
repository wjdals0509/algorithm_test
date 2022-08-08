def d(n):
    n = n + sum(map(int, str(n))) 
    #생성자n을 이용해 d(n)을 만드는 수식
    #int로 들어온 n을 str로 형변환 -> 문자열이 됨(iterable)
    #map()을 이용해 다시 int로 형변환
    #sum()을 이용해 각 자리 수의 합 구할 수 있음
    return n
nonSelfNum=set() 
#셀프 넘버가 아닌(생성자가 있는) 수들이 들어갈 집합(set)
#중복을 없애기 위해 set()으로
for i in range(1,10001):
    nonSelfNum.add(d(i)) 
    #add는 집합 자료형(추가)
    #집합에 들어갈 수 들을 찾아서 넣음
for j in range(1,10001):
    if j not in nonSelfNum: #셀프 넘버가 아닌 수들 = 셀프 넘버
        print(j) #셀프 넘버 출력
