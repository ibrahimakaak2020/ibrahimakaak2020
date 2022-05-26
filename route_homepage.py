from fastapi import APIRouter, requests
from fastapi import Request
from fastapi import responses
from fastapi.templating import Jinja2Templates
from fastapi import responses , status
from db.repository.users import get_users
from db.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request,msg:str=None,db: Session = Depends(get_db)):
	users=get_users(db=db)
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request,"status":status,'msg':msg,'users':users})

# @general_pages_router.post("/")
# async def home(request: Request):
    
# 	return responses.RedirectResponse("/?msg=Successfully-Registered",status_code=status.HTTP_302_FOUND) 
