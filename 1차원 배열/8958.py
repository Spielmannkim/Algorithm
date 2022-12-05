a = int(input()) # 테스트 케이스의 개수
for i in range(a): # 테스트 케이스의 개수만큼 반복
    b = input() # 문자열 b를 입력
    s = list(b) # 문자열 b들로 이루어진 리스트 s 생성
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)

# 이번 문제는 매우 어려웠다.
# O와X를 따로 입력받아야겠다고 생각하며 문제를 시작했는데
# X는 필요없고 O가 몇개인지가 중요했다.
# 아직 for문이 익숙치 않다.
# 머릿속에 for문이 완전히 자리잡을 때까지 조금 더 문제를 복습해야겠다.