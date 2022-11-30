while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B) #마지막 0 0 을 입력했을 때 출력값이 안나오고 종료시키려면 print를 마지막 줄에서 해야한다. 0을 출력하고 종료하고 싶다면 if 윗 줄에 껴넣어야 한다.