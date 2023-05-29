# 연산의 나머지는 나머지들의 연산이다라는 아이디어를 사용해 solve
# pow 내장 함수는 거듭제곱만 사용해봤는데 3번째 인자가 나머지 연산을 해준다는 것을 이용함
import sys

K, P, N = map(int, sys.stdin.readline().split())

virus = K * pow(P, N, 1000000007) # pow 내장함수를 통해서 pow(기본 수, 거듭제곱 하려는 수, 나머지 연산 하는 수)

final_virus = virus % 1000000007 # 결과 값의 나머지

print(final_virus)