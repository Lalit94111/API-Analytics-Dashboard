from fastapi import Request
from sqlalchemy.orm import Session
from datetime import datetime
from user_agents import parse
from models import Item,API_Info
from sqlalchemy import func
import schemas
from datetime import datetime

async def log_api_request(request : Request,db:Session):
    timestamp = datetime.now()
    client_ip = request.client.host
    user_agent = request.headers.get('user-agent')
    method = request.method
    endpoint = request.url.path
    payload = None
    content_type = request.headers.get('content-type')
    ua = parse(user_agent)
    browser_name = ua.browser.family 
    os_name = ua.os.family 

    if os_name=='Other':
        os_name = browser_name

    if method in ['PUT','POST']:
        request_body = await request.body()
        payload = request_body.decode() if request_body else None
        request._body = request_body

    # print(timestamp,client_ip,browser_name,os_name,method,endpoint,payload,content_type)

    new_api_data = API_Info(
        request_type = method,
        request_time = timestamp,
        api_endpoint = endpoint,
        payload = payload,
        user_agent = browser_name,
        operating_system = os_name,
        ip_address = client_ip,
        content_type = content_type
    )

    db.add(new_api_data)
    db.commit()

def get_data_by_browser(db:Session):
    data = db.query(API_Info.user_agent,func.count(API_Info.id).label('count'))\
             .group_by(API_Info.user_agent)\
             .all()
    
    return data

def get_all_request_data(db:Session,start_date:str,end_date:str):
    query = db.query(API_Info)
    # print(start_date,end_date)
    if start_date!='null':
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(API_Info.request_time >= start_date_obj)

    if end_date!='null':
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(API_Info.request_time <= end_date_obj)

    data = query.all()
    
    return data

def get_data_bar_chart(db:Session):
    user_agent = db.query(API_Info.user_agent,func.count(API_Info.id).label('count'))\
             .group_by(API_Info.user_agent)\
             .all()
    
    operating_system = db.query(API_Info.operating_system,func.count(API_Info.id).label('count'))\
             .group_by(API_Info.operating_system)\
             .all()
    
    api_endpoint = db.query(API_Info.api_endpoint,func.count(API_Info.id).label('count'))\
             .group_by(API_Info.api_endpoint)\
             .all()
    
    request_type = db.query(API_Info.request_type,func.count(API_Info.id).label('count'))\
             .group_by(API_Info.request_type)\
             .all()
    
    return {'user_agent' : user_agent,'operating_system':operating_system,'api_endpoint':api_endpoint,'request_type':request_type}

def get_items(db: Session):
    return db.query(Item).all()

def get_item_by_id( item_id: int,db: Session,):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(item:schemas.Item,db: Session):
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(item_id: int,item:schemas.ItemUpdate,db: Session):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        for field,value in item.model_dump(exclude_unset=True).items():
            setattr(db_item,field,value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item( item_id: int,db: Session):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
    