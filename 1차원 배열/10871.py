# X보다 작은 수들을 출력

N, X = map(int, input().split()) # 정수의 개수 N, 찾아야하는 정수 X
A = list(map(int, input().split())) # 정수의 수열 A
for i in range(N): # for문을 N번 반복
    if A[i] < X: # 만약 A의 수열 중 X보다 작다면
        print(A[i], end=" ") # 그 해당하는 A[i]를(정수를) 출력하고 출력을 한줄로 이어지게하는 end=" "를 사용함.