n = int(input()) # 테스트 개수

for _ in range(n): # n번만큼 반복
    ox_list = list(input()) # 입력받은 값들을 ox_list라는 리스트에 저장
    score = 0  # 점수 0점으로 세팅
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list: # ox_list의 값들을 순서대로 ox변수에 저장
        if ox == 'O': # 만약 처음 입력받은 리스트에 O가 있고
            score += 1  # 그 O가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score(총점) = sum_score(총점) + score(점수)
        else:
            score = 0 # O가 아닐경우(X일경우) 점수는 0점으로 다시 0가 나올때까지 리셋된다.
    print(sum_score) # 총점은?