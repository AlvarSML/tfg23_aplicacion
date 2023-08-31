from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, imagen, models, states

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])

api_router.include_router(imagen.router, prefix="/radiogrfias", tags=["radiografias"])
api_router.include_router(models.router, prefix="/models", tags=["modelos"])
api_router.include_router(states.router, prefix="/states", tags=["estados","modelos"])