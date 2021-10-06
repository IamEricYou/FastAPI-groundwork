from typing import Optional
from fastapi import FastAPI
from enum import Enum

from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print(e)
        return JSONResponse({"status": str(e)}, status_code=500)

app.middleware('http')(catch_exceptions_middleware)

class EnumClass(str, Enum):
    a = "a"
    b = "b"
    c = "c"

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/enum/{enum_name}")
async def read_enum(enum_name: EnumClass):
    return EnumClass.value