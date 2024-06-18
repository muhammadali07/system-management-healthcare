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

async def getListAccount(page, limit, keyword, session):
    try:
        terms = []
        if keyword not in (None, ""):
            terms.append(
                or_(
                    (user_models.Users.username.ilike(f"%{keyword.lower()}%")),
                    (user_models.Users.role.ilike(f"%{keyword.lower()}%")),
                    (user_models.Users.nama_lengkap.ilike(f"%{keyword.lower()}%")),
                    (user_models.Users.email.ilike(f"%{keyword.lower()}%"))
                )
            )

        offset = (page*limit)
        sql = select(user_models.Users).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e
    

async def GetUserDetailByEmail(keyword, session):
    try:
        sql = select(user_models.Users).where(user_models.Users.email == keyword)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().first()
        
        return data, None
    except Exception as e:
        return None, e
    
async def GetUserDetailByUsername(keyword, session):
    try:
        sql = select(user_models.Users).where(user_models.Users.username == keyword)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().first()
        
        return data, None
    except Exception as e:
        return None, e
    
async def UpdateUserDetail(username, nama_lengkap, email, password, no_ktp, no_hp, alamat, session):
    try:
        terms = []
        if username not in (None, ""):
            terms.append(
                or_(
                    (user_models.Users.username.ilike(f"%{username.lower()}%")),
                )
            )

        sql =(
            update(user_models.Users)
            .where(user_models.Users.username == username)
            .values(nama_lengkap = nama_lengkap,
                    email = email,
                    password = password,
                    no_ktp = no_ktp,
                    no_hp = no_hp,
                    alamat = alamat)
        )
        await session.execute(sql)
        await session.commit()
        
        return no_hp, None
    except Exception as e:
        return None, e
    
async def DeleteAccount(username, session) :
    try:
        sql =(
        delete(user_models.Users)
        .where(user_models.Users.username == username)
        )
        await session.execute(sql)
        await session.commit()
        
        return username, None
    except Exception as e:
        return None, e
    
