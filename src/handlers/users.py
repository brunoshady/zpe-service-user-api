from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from src.schemas.user import User, UserCreate
from src.schemas.user_roles import UserRolesPatch
from src.services import repository
from src.services.database import get_db
from src.utils.json_response import PrettyJSONResponse

users_router = APIRouter()


@users_router.get("/")
async def root():
    return RedirectResponse(url="/v1/users", status_code=303)


@users_router.get("/v1/users", response_model=list[User], response_class=PrettyJSONResponse)
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = repository.get_users(db, skip=skip, limit=limit)
    return users


@users_router.get("/v1/users/{user_id}", response_model=User, response_class=PrettyJSONResponse)
async def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = repository.get_user(db, user_id)
    return user


@users_router.post("/v1/users", status_code=201, response_class=PrettyJSONResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repository.create_user(db, user)
    return {"message": "User successfully created."}


@users_router.patch("/v1/users/{user_id}/roles", status_code=200, response_class=PrettyJSONResponse)
async def update_user_roles(user_id: UUID, user_roles: UserRolesPatch, db: Session = Depends(get_db)):
    repository.update_user_roles(db, user_id, user_roles)
    return {"message": "Roles successfully updated."}


@users_router.delete("/v1/users/{user_id}", status_code=200, response_class=PrettyJSONResponse)
async def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    repository.delete_user(db, user_id)
    return {"message": "User successfully deleted."}
