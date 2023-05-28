# 출처 : https://hwisaek.tistory.com/entry/Softeer-%EA%B8%88%EA%B3%A0%ED%84%B8%EC%9D%B4-Python
import sys

input = sys.stdin.readline

w, n = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(n)]

jewels.sort(key=lambda x: x[1], reverse=True)

answer = 0
for weight, price in jewels:
    if w > weight:
        answer += weight * price
        w -= weight
    else:
        answer += w * price
        break

print(answer)