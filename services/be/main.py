from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.post("/register")
async def regisAkun(
    request: regisAkun,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.regis_user(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)