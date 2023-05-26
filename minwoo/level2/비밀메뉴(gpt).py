def check_secret_menu(M, N, K, secret_operations, user_operations):
    # 비밀 메뉴 작동 방법을 문자열로 변환하여 검색을 용이하게 함
    secret_str = ' '.join(map(str, secret_operations))
    user_str = ' '.join(map(str, user_operations))

    # 사용자 작동 방법에서 비밀 메뉴 작동 방법이 존재하는지 확인
    if secret_str in user_str:
        return "secret"
    else:
        return "normal"


# 입력 받기
M, N, K = map(int, input().split())
secret_operations = list(map(int, input().split()))
user_operations = list(map(int, input().split()))

# 결과 출력
result = check_secret_menu(M, N, K, secret_operations, user_operations)
print(result)
