from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    ID: str
    type: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def read_all_users():
    return {"list": ["all", "the", "users"]}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/users/")
async def create_user(user: User):
    return user

@app.put("/users/{user_id}")
async def create_user(user_id: int, user: User):
    return {"user_id": user_id, **user.dict()}