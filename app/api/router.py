from fastapi import APIRouter
from .login import login

userRouter = APIRouter(prefix='/api/v1', tags=['用户相关'])

userRouter.post(path='/login', description='登录', summary='用户登录')(login)
