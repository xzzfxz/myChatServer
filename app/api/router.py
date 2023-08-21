from fastapi import APIRouter
from .userRouter import login, getUsers, test, getCurrentUser, token

userRouter = APIRouter(prefix='/api/v1/user', tags=['用户相关'])

userRouter.post(path='/test', summary='token')(test)
userRouter.post(path='/token', summary='token')(token)
userRouter.post(path='/login', summary='用户登录')(login)
userRouter.get(path='/getUsers', summary='获取所有用户')(getUsers)
userRouter.get(path='/getCurrentUser', summary='获取当前用户')(getCurrentUser)
