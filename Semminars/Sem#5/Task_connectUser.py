def login(user):
    # admin = 1
    
    # if user.is_active:
    #     if user == admin:
    #         print('OK')
    #     else:
    #         print('Не админ')
    # else:
    #     print('user not active')
    
    # пишем рекурсией

    if not user.is_active:
        print('user not active')
        return -1
    
    if user != admin:
        print('Не админ')
        return -2
    
    print('OK')
    return 0