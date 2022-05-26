from db.repository.users import create_new_user
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
    return templates.TemplateResponse("general_pages/register.html", {"request": request})


@router.post("/register/")
async def register(request: Request, db: Session = Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            staffno=form.staffno, staffname=form.staffname, password=form.password
        )
        try:
            user = create_new_user(user=user, db=db)
            return responses.RedirectResponse(
                "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND,headers={'stafno':form.staffno}
            )  # default is post request, to use get request added status code 302
        except IntegrityError:
            form.__dict__.get("errors").append("User  already register with this staff No:  "+ form.staffno)
            return templates.TemplateResponse("general_pages/register.html", form.__dict__)
    return templates.TemplateResponse("general_pages/register.html", form.__dict__)
