from app.api.router import userRouter
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(userRouter)

if (__name__ == '__main__'):
    uvicorn.run(app='main:app', reload=True)
