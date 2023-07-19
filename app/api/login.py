
def login(username: str, password: str):
    """用户管理

    Args:
        username (string): 用户名
        password (string): 密码
    """
    print(username, password)
    return {"username": username, "password": password}
