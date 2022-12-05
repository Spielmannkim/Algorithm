# 평균은 넘겠지

C = int(input()) # 시험과목 개수
for i in range(C): # 시험과목 개수만큼 반복
    N =  int(input()) # 학생수 N
    score = map(int, input().split()) # 학생 별 점수
AVG = sum(score)/N # 평균 = 학생별 점수 총합sum(score) / 학생수 N
# 지금 해결해야할 문제 = AVG에 마지막 과목 평균만 구해지는데 과목별 평균을 구하고 싶음.
print(AVG)