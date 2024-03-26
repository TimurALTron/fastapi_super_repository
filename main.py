
from fastapi import FastAPI

from contextlib import asynccontextmanager

from router import  router as tasks_router
import database


@asynccontextmanager
async def lifespan(app:FastAPI):
    await database.delete_tables()
    print("База очищена")
    await database.create_tables()
    print("База готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)




