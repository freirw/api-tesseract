from sqlalchemy import Column, Integer, String
from database import Base

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True, nullable=False)
    content = Column(String, nullable=False)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    naturalidade = Column(String, nullable=False)
    orgao_emissor = Column(String, nullable=False)
