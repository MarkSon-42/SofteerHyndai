# 문제가 쉽고 재밌다. 반복문 규칙 찾기 연습문제로 참 좋은듯
# ??? 못풀었다. 테케 2개빼고 전부 틀린다.

N = int(input())
init = 4
step_1 = init
step_2 = 1
result = 0
for i in range(1, N + 1):
    if i == 1:
        step_1 = init * 1
        result = init + step_1 + step_2

    else:
        init = result
        step_1 *= 3
        step_2 *= 4
        result = init + step_1 + step_2

print(result)

