from app.api.router import userRouter
from fastapi import FastAPI
import uvicorn
from app.utils.logger import logger
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(userRouter)

# 跨域设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.middleware("http")
async def log_request_params(request, call_next):
    logger.info(f'请求的url: {request.url}')
    logger.info(f'请求的方法: {request.method}')
    response = await call_next(request)
    return response

if (__name__ == '__main__'):
    uvicorn.run(app='main:app', reload=True)
