# 평균은 넘겠지
# 이번 문제는 여러 시험과목별(n)로 학생수와 받은점수를 입력하여 평균을 구한 뒤 평균 이상인 학생의 비율을 출력하는 문제.


n = int(input()) # 시험과목 개수

    # 1.점수의 평균 구하기
    
for _ in range(n): # 시험과목 개수만큼 반복
    nums = list(map(int, input().split())) # 학생 별 점수
    avg = sum(nums[1:])/nums[0] # 평균을 구함 (nums[0] = 학생수, nums[1:] = 점수)
    
    # 2.평균 이상인 학생 수 구하기
    
    cnt = 0
    for score in nums[1:]: # 각 점수는 score변수에 선언하고 위에서 구한 평균값을 이용해서
        if score > avg: # 평균보다 클 경우
            cnt += 1 # cnt변수에 1씩 더해줌
    
    # 3.평균보다 높은 점수를 받은 학생 비율을 구하고 출력문 작성
            
    rate = cnt/nums[0] * 100 # 평균 이상인 학생 수(cnt) / 학생 수 * 100
    print(f'{rate:.3f}%') # .3f = 소숫점 셋째 자리까지, f스트링 사용하여 스트링 속 변수 사용