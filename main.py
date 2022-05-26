from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles #new
from core.config import  settings
from route_homepage import general_pages_router
from db.database.database  import db_engine #newp
from db.models.models import *
from webapps.base import api_router as web_app_router
from db.database.database import Base  #new

def include_router(app):
    app.include_router(general_pages_router)
    app.include_router(web_app_router)

def create_tables():
    Base.metadata.create_all(bind= db_engine)
    
  

def configure_static(app):  #new
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables() 
    
    configure_static(app) #new
    return app

    

app = start_application()
