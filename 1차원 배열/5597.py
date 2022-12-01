n = [i for i in range(1, 31)] # 1-30까지 정수 리스트

for _ in range(28): # 28번 반복
    all = int(input()) # 참석한 학생번호 하나씩 입력
    n.remove(all) # 전체 학생n 중 참석한 학생all을 빼서 최종 결석자 리스트 생성
    
print(min(n)) # 결석자중 최솟값을 통해 번호앞자리 결석자 출력
print(max(n)) # 결석자중 최댓값을 통해 번호뒷자리 결석자 출력