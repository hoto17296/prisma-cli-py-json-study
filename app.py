"""fastapi dev コマンドでサーバを起動できる"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from prisma import Prisma
from prisma.models import Parent

db = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/parent")
async def get_parent() -> Parent:
    parent = await db.parent.find_first(include={"children": True})
    if parent is None:
        raise HTTPException(status_code=404)
    return parent
