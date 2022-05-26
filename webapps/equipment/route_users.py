from db.repository.equipments import create_new_user , get_user_by_staffno
from db.database.database import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.templating import Jinja2Templates
from db.schemas.schemas import UserCreate 
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from webapps.users.forms import UserCreateForm


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse("general_pages/register.html", {"request": request ,"user":None})


@router.post("/register/",response_model=get_user_by_staffno)
async def register(request: Request, db: Session = Depends(get_db),user1=get_user_by_staffno):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            staffno=form.staffno, staffname=form.staffname, password=form.password
        )
        try:
            user = create_new_user(user=user, db=db)
            get_user=user1(user.staffno,db=db)
            print(get_user)
            return responses.RedirectResponse(
                "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND,context={'user':get_user}
            )  # default is post request, to use get request added status code 302
        except IntegrityError:
            form.__dict__.get("errors").append("User  already register with this staff No:  "+ form.staffno)
            return templates.TemplateResponse("general_pages/register.html", form.__dict__)
    return templates.TemplateResponse("general_pages/register.html", form.__dict__)
