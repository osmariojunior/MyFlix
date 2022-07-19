from sqlalchemy import Column, Integer, String, DateTime
from src.infra.sqlalchemy.config.database import Base

class Serie(Base):
    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(String)
    gender = Column(String)
    qtd_temp = Column(Integer)