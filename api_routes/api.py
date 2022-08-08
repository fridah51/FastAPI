from fastapi import APIRouter
from .todo import todo_router
from .user import user_router



router = APIRouter()


router.include_router(todo_router, prefix = "/todos", tags=["TODOS"], )
router.include_router(user_router, prefix = "/users", tags=["USER"], )