from database import Base
from sqlalchemy import Column,Integer,String,VARCHAR,DateTime,Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Item(Base):
    __tablename__="items"

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(100),nullable=False)
    content = Column(VARCHAR(200),nullable=False)


class API_Info(Base):
    __tablename__='API_Info'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    request_type = Column(String(10),nullable=False) 
    request_time = Column(DateTime,nullable=False)
    api_endpoint = Column(VARCHAR(200),nullable=False)
    payload = Column(Text,nullable=True) #Request Body (if there)
    user_agent = Column(String(50),nullable=False) #Chrome , Postman , Safari
    operating_system = Column(String(50),nullable=False)
    ip_address = Column(String(20),nullable=False)
    content_type = Column(String(20),nullable=True) #Cotent type Application JSON
