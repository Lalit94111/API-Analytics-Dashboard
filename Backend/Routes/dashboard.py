from fastapi import APIRouter,Depends,Query
from crud import get_data_by_browser,get_all_request_data,get_data_bar_chart
from sqlalchemy.orm import Session
from utils import get_db
from schemas import PieChartData,APIInfo,UserAgent,APIEndpoint,RequestType,OperatingSystem,BarGraphData
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.get("/dashboard/piechart/",response_model=list[PieChartData])
def get_piechart_data_by_browsers(db:Session = Depends(get_db)):
    data = get_data_by_browser(db)
    result = []
    for item in data:
        item = item._asdict()
        validated_data = PieChartData(**item)
        result.append(validated_data)
    return result

@router.get("/dashboard/request_table/",response_model=list[APIInfo])
def get_requests_data(db:Session = Depends(get_db)
                      ,start_date: Optional[str] = Query(None, description="Start date for filtering requests")
                      ,end_date: Optional[str] = Query(None, description="End date for filtering requests")):
    # print(start_date,end_date)
    data = get_all_request_data(db,start_date,end_date)
    result = []

    for item in data:
        validated_data = APIInfo(**item.__dict__)
        result.append(validated_data)

    return result

def validate_data(value,Model):
    result = []
    for item in value:
        item = item._asdict()
        validated_data = Model(**item)
        result.append(validated_data)
    return result

@router.get("/dashboard/bargraph/",response_model=BarGraphData)
def get_bargraph_data(db:Session = Depends(get_db)):
    data = get_data_bar_chart(db)
    result = {}
    for key,value in data.items():
        if key=='user_agent':
            validated_data = validate_data(value,UserAgent)
            result[key] = validated_data
        elif key=='operating_system':
            validated_data = validate_data(value,OperatingSystem)
            result[key] = validated_data
        elif key=='api_endpoint':
            validated_data = validate_data(value,APIEndpoint)
            result[key] = validated_data
        else:
            validated_data = validate_data(value,RequestType)
            result[key] = validated_data
    return result