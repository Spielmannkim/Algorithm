
# 빠른 A+B

# for문을 사용할 때 입력받거나 출력할 때 입출력 방식을 빠르게 하는 함수.
# input()대신 sys.stdin.readline()을 사용한다.

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)