
from fastapi import Query
from app.dbs.db import Database
from app.models.userInfo import User

database = Database()
database.get_db_connection()


def login(username: str = Query(description="用户名"), password: str = Query(description="密码")):
    """用户登录
    Args:
        username (string): 用户名
        password (string): 密码
    """
    print(username, password)
    return {"username": username, "password": password}


async def getUsers():
    '''获取所有用户
    '''
    session = database.get_db_session()
    data = session.query(User).all()
    for row in data:
        row.createdTime = str(row.createdTime)
    return data
