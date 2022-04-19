from fastapi import FastAPI
from api.users import users

app = FastAPI()

app.include_router(users)