def check_secret_menu(M, N, K, secret_operations, user_operations):
    secret_str = ' '.join(map(str, secret_operations))
    user_str = ' '.join(map(str, user_operations))

    if secret_str in user_str[:N]:
        return "secret"
    else:
        return "normal"
