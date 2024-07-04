from fastapi import APIRouter,Depends
from utils import get_db
from schemas import Item,ItemDB,ItemUpdate
from sqlalchemy.orm import Session
import crud

router = APIRouter()

@router.get("/items/",response_model=list[ItemDB])
async def read_items(db:Session = Depends(get_db)):
    items = crud.get_items(db)
    return items

@router.get("/items/{itemID}/",response_model=ItemDB)
async def read_item(itemID:int,db:Session = Depends(get_db)):
    item = crud.get_item_by_id(itemID,db)
    return item

@router.post("/items/",response_model=ItemDB)
async def create_Item(item:Item,db:Session = Depends(get_db)):
    item = crud.create_item(item,db)
    return item

@router.put("/items/{itemID}/",response_model=ItemDB)
async def update_item(itemID:int,item:ItemUpdate,db:Session = Depends(get_db)):
    item = crud.update_item(itemID,item,db)
    return item

@router.delete("/items/{itemID}/",response_model=ItemDB)
async def delete_item(itemID:int,db:Session = Depends(get_db)):
    item = crud.delete_item(itemID,db)
    return item