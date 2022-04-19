from fastapi import FastAPI, APIRouter
from typing import List

from api.models import User

fake_user_db = [
    {
        'id': 'asda123',
        'username': 'bautiKPO',
        'mail': 'jbrodriguez@fi.uba.ar',
        'firstname': 'Bautista',
        'lastname': 'Rodriguez',
        'type': 'Listener'
    }
]

users = APIRouter()

@users.get('/', response_model=list[User])
async def index():
    return fake_user_db

@users.post('/', status_code=201)
async def add_user(payload: User):
    user = payload.dict()
    fake_user_db.append(user)
    return {'id': len(fake_user_db) - 1}

@users.put('/{id}')
async def update_user(id: int, payload: User):
    user = payload.dict()
    users_length = len(fake_user_db)
    if 0 <= id <= users_length:
        fake_user_db[id] = user
        return None
    raise HTTPException(status_code=404, detail="User with given id not found.")

@users.delete('/{id}')
async def delete_user(id: int):
    users_length = len(fake_user_db)
    if 0 <= id <= users_length:
        del fake_user_db[id]
        return None
    raise HTTPException(status_code=404, detail="User with given id not found.")