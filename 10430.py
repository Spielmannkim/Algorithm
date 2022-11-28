#map함수를 사용하지 않았을경우
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n') #sep='\n' 은 엔터

#map함수 사용으로 코드를 짧게
a,b,c=map(int, input().split())
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n') #sep='\n' 은 엔터