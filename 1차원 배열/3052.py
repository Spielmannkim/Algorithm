arr = [] # 빈 배열 생성
for i in range(10): # 10번 반복
    n = int(input()) # n에 정수 입력받음(10번)
    arr.append(n % 42) # 빈 배열에 입력받은 n 나누기 42의 나머지를 추가함
arr = set(arr) # set함수로 arr변수에 있는 배열을 집합으로 바꿈 [] -> {}
print(len(arr)) # len함수로 문자열의 길이를 출력