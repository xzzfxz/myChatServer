from fastapi import APIRouter
from .login import login, getUsers

userRouter = APIRouter(prefix='/api/v1/user', tags=['用户相关'])

userRouter.post(path='/login', summary='用户登录')(login)
userRouter.get(path='/getUsers', summary='获取所有用户')(getUsers)
