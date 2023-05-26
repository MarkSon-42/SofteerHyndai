def check_secret_menu(M, N, K, secret_operations, user_operations):
    secret_set = set(secret_operations)
    user_set = set(user_operations[:N])

    if secret_set.intersection(user_set) == secret_set:
        return "secret"
    else:
        return "normal"
