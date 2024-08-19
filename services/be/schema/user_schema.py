from pydantic import BaseModel

class account(BaseModel):
    username : str = "nightingale123"
    nama_lengkap : str =" Florence Nightingale"
    email : str = "nightingael123@gmail.com"
    password : str = "123456"
    no_ktp : str = "1234567891234"
    no_hp : str = "0811111111111"
    alamat : str = "England"
    role : str = "Pasien"
