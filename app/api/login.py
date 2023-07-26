
from fastapi import Query


def login(username: str = Query(description="用户名"), password: str = Query(description="密码")):
    """用户登录
    Args:
        username (string): 用户名
        password (string): 密码
    """
    print(username, password)
    return {"username": username, "password": password}
