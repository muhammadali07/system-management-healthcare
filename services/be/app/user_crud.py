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
            
            resvalidasicreateaccusername,e = await user_datastore.GetUserDetailByUsername(data.username, session)
            if resvalidasicreateaccusername not in (None,{}):
                raise Exception("Username sudah digunakan! silahkan masukkan username yang baru")

            resvalidasicreateaccemail,e = await user_datastore.GetUserDetailByEmail(data.email, session)
            if resvalidasicreateaccemail not in (None,{}):
                raise Exception("Email sudah digunakan! silahkan masukkan email yang baru")


            resCreateAccount, e = await user_datastore.registNewAccount(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resCreateAccount, None


        except Exception as e:
            return data, e
        
        
async def get_list_account(page: int, limit:int, keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetListAccount, e = await user_datastore.getListAccount(page, limit, keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetListAccount, None


        except Exception as e:
            return resgetListAccount, e
        

async def get_list_user_detail(keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetUserDetailByEmail, e = await user_datastore.GetUserDetail(keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetUserDetailByEmail, None


        except Exception as e:
            return None, e
        
async def update_user_detail(username: str, nama_lengkap: str, email: str, password: str, no_ktp: str, no_hp: str, alamat: str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            updateUserDetail, e = await user_datastore.UpdateUserDetail(username, nama_lengkap, email, password, no_ktp, no_hp, alamat, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return updateUserDetail, None


        except Exception as e:
            return None, e
        
async def Delete_Account(username:str,  db_session:AsyncSession):
    async with db_session as session:
        try:  

            DeleteAccount, e = await user_datastore.DeleteAccount(username,  session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return DeleteAccount, None


        except Exception as e:
            return None, e
