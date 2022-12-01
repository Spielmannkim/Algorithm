numbers = [] # numbers라는 비어있는 리스트
for _ in range(9): # 9번 반복
    i = int(input()) # i에 정수 입력받음
    numbers.append(i) # 비어있는 리스트에 i의 정수들을 덧붙인다는 의미
    
print(max(numbers)) # 리스트중 최댓값

# 리스트속 원하는게 몇번째 있는지 알고 싶을땐 index() 함수 사용.
# 여기서 원하는 건 최대값이 몇번째 있는지이기에 리스트의 시작이0이니 +1을 붙임.
print(numbers.index(max(numbers))+1)
