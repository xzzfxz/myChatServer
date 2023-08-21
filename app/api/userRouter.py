
from fastapi import Depends, HTTPException, Query
from app.dbs.db import Database
from app.models.userInfo import User
from app.schemas.userScheme import UserInDB
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

database = Database()
database.get_db_connection()


def fake_decode_token(token):
    return User(username=token + 'fakedecoded', phone=18721981234)


def fake_hash_password(password: str):
    return password


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


async def test(token: str = Depends(oauth2_scheme)):
    return {"token": token}


def login(username: str = Query(description="用户名"), password: str = Query(description="密码")):
    """用户登录
    Args:
        username (string): 用户名
        password (string): 密码
    """
    print(username, password)
    return {"username": username, "password": password}


async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    session = database.get_db_session()
    data = session.query(User).filter(
        User.account == form_data.username).one_or_none()
    if not data:
        raise HTTPException(status_code=400, detail='用户名或密码错误')
    user = UserInDB(**data.__dict__)
    hashedPassword = fake_hash_password(form_data.password)
    if not hashedPassword == user.password:
        raise HTTPException(status_code=400, detail='用户名或密码错误')
    return data


async def getUsers():
    '''获取所有用户
    '''
    session = database.get_db_session()
    data = session.query(User).all()
    for row in data:
        row.createdTime = str(row.createdTime)
    return data


async def getCurrentUser(currentUser: User = Depends(get_current_user)):
    """获取当前用户
    Args:
        currentUser (User, optional): _description_. Defaults to Depends(get_current_user).

    Returns:
        _type_: User
    """
    return currentUser
