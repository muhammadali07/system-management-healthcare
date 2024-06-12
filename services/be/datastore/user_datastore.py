from models import user_models
from sqlalchemy import select, or_, and_, update, delete
from api import user_api

async def registNewAccount(data, session):
    try:
        paramsInsert = user_models.Users(
            username = data.username,
            nama_lengkap = data.nama_lengkap,
            email = data.email,
            password= data.password,
            no_ktp = data.no_ktp,
            no_hp = data.no_hp,
            alamat = data.alamat,
            role = data.role
        )

        session.add(paramsInsert)
        return data, None
    except Exception as e:
        return data, e