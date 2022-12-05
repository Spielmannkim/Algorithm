N = int(input()) # 시험 본 과목의 개수
point = list(map(int, input().split())) # 각 시험 별 받은 점수
MAXPOINT = max(point) # 점수 중 최댓값

FAKE = [] # 조작된 점수 리스트
for score in point: # point(입력받은 시험점수) 첫번째 점수 부터 순서대로 score에 넣고
    FAKE.append(score / MAXPOINT * 100) # 모든 점수를 score / MAXPOINT * 100 을 해서 FAKE라는 조작된 점수들을 만들고
AVG = sum(FAKE)/N # 평균점수 = FAKE (리스트 들)의 합 나누기 N (과목수)
print(AVG) # FAKE의 평균값을 출력