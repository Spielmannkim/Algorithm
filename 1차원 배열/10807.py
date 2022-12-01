N = int(input()) # 정수의 개수
n_list = list(map(int, input().split())) # 정수 리스트
v = int(input()) # 찾으려는 정수

print(n_list.count(v)) # 정수 리스트 중 v가 몇개인지 카운트