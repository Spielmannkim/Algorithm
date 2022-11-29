# A+B-7
import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #", i+1, ": ", A+B, sep="")
    
# 풀이 없이 맞췄다!!