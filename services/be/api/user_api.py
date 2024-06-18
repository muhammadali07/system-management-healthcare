from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import user_crud
from utils import RespApp, get_async_session
from schema import account



router = APIRouter()

@router.post("/regis-new-account")
async def RegistNewAccount(
    request: account,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.create_new_account(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-new-account")
async def GetListNewAccount(
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_account(page, limit, keyword, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-user-detail")
async def GetListUserDetail(
    params: str = "masukkan username atau email",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_user_detail(params, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.put("/update-user-detail")
async def UpdateUserDetail(
    username: str = None,
    nama_lengkap: str = None,
    email: str = None,
    password: str = None,
    no_ktp: str = None,
    no_hp: str = None,
    alamat: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.update_user_detail(username, nama_lengkap, email, password, no_ktp, no_hp, alamat, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.delete("/Delete-Account")
async def DeleteAccount(
    username: str = "masukkan username akun yang akan dihapus",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.Delete_Account(username, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data = None)
    
    return RespApp(status="00", message="success", data=out_resp)

