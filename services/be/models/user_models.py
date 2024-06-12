from sqlalchemy import Column, String, BigInteger, Text, DateTime, Integer, Numeric
from datetime import datetime
from utils import Base


class Users(Base):
    __tablename__ = 'users_healthcare'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(50))
    nama_lengkap = Column(String(100))
    email = Column(String(50))
    password = Column(Text)
    no_ktp = Column(String(16))
    no_hp = Column(String(13))
    alamat = Column(Text)
    role = Column(String(10))
    create_at = Column(DateTime, default=datetime.now())