while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break # try와 except를 while문에서 이렇게 사용한다.