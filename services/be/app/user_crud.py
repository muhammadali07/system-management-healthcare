from sqlalchemy.ext.asyncio import AsyncSession
from datastore import user_datastore
from schema import account

async def create_new_account(data: account, db_session:AsyncSession):
    async with db_session as session:
        try:
            if data.username == "" :
                raise Exception("username harus di isi")
            
            if data.nama_lengkap == "" :
                raise Exception("nama lengkap harus di isi")

            if data.email == "" :
                raise Exception("email harus di isi")
            
            if data.password == "" :
                raise Exception("password harus di isi")

            if data.no_ktp == "" :
                raise Exception("no. ktp harus di isi")

            if data.no_hp == "" :
                raise Exception("no. hp harus di isi")
            
            if data.alamat == "" :
                raise Exception("alamat harus di isi")

            if data.role == "" :
                raise Exception("role harus di isi")

            resCreateAccount, e = await user_datastore.registNewAccount(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resCreateAccount, None


        except Exception as e:
            return data, e