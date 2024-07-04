from pydantic import BaseModel,Field
from typing import Optional,List
from datetime import datetime
from uuid import UUID

class Item(BaseModel):
    title: str = Field(..., description="The title of the item")
    content: str = Field(..., description="The content of the item")

class ItemUpdate(BaseModel):
    title: str = Field(None, description="The updated title of the item")
    content: str = Field(None, description="The updated content of the item")

class ItemDB(Item):
    id: int

    class Config:
        from_attributes = True

class PieChartData(BaseModel):
    user_agent : str
    count : int

    class Config:
        from_attributes = True

class UserAgent(BaseModel):
    user_agent : str
    count : int

class OperatingSystem(BaseModel):
    operating_system : str
    count : int

class APIEndpoint(BaseModel):
    api_endpoint : str
    count : int

class RequestType(BaseModel):
    request_type : str
    count : int

class BarGraphData(BaseModel):
    user_agent : List[UserAgent]
    operating_system : List[OperatingSystem]
    api_endpoint : List[APIEndpoint]
    request_type : List[RequestType]

class APIInfo(BaseModel):
    id : UUID
    request_type: str = Field(..., max_length=10)
    request_time: datetime
    api_endpoint: str = Field(..., max_length=200)
    payload: Optional[str] = None
    user_agent: str = Field(..., max_length=50)
    operating_system: str = Field(..., max_length=50)
    ip_address: str = Field(..., max_length=20)
    content_type: Optional[str] = Field(None, max_length=20)

    class Config:
        from_attributes = True
