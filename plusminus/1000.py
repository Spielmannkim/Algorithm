#입력데이터의 갯수가 많은 문제를 풀 때 input() 함수를 사용하면 동작이 느려서 readline함수를 사용 

#1 sys 라이브러리 임포트
import sys 

#2 stadin.readline() 함수
#3 split(' ') 함수를 사용하여 입력데이터 사이 한칸을 띄움
A, B = sys.stdin.readline().split(' ') 

#4 정수는 int()
print(int(A)+int(B)) 

# 사실 실제 1000번문제를 풀때 오답이었던이유는 동작속도때문이 아닌 input()을 사용할때 split()를 사용하지 않아서였다... 덕분에 sys라이브러리랑 stadin.readline()펑션은 확실히 익힌것같다 keep 삽 to the 질 Gazua 

# 따라서 이렇게 간단히 풀 수 있다.
a,b=input().split()
a=int(a)
b=int(b)
print(a+b) 

#심지어는 딱 두줄도 가능하다..
a,b=input().split()
print(int(a)+int(b))