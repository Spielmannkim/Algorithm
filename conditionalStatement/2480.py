a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif c == a:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100) #max함수 사용법
    
#드디어 해설 없이 푸는 첫 문제이려나 싶었는데 제일 큰눈 구하는 방법을 몰라서 검색해보았다.
#다행히도 배운적 없는 max, min 함수가 필요한 문제였다.