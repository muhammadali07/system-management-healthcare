from fastapi import APIRouter

from app import testing_crud
from utils import RespApp
from schema import account


router = APIRouter()

@router.get("/")
async def greeting():
    out_resp = await testing_crud.Greeting()
    return RespApp(status="00", message="success", data=out_resp)