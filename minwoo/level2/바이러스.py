# 일단 제약조건만 봐도 시간복잡도를 신경쓰라는 것을 알 수 있는 문제다.
# 따라서 그냥 나머지를 계산해서 출력하면 안된다

# ...?

# https://fre2-dom.tistory.com/21

import sys

k, p, n = list(map(int,sys.stdin.readline().split()))

# 총 시간동안 바이러스를 증가시킨다.
for i in range(n):
    k = (k * p) % 1000000007

print(k)