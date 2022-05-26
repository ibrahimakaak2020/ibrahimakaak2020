from typing import List
from typing import Optional

from fastapi import Request


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.staffno: Optional[str] = None
        self.staffname: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.staffno = form.get("staffno")
        self.staffname = form.get("staffname")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.staffno :
            self.errors.append("staff NO should be Not Null ..")
        if not len(self.staffname) > 3:
            self.errors.append("Username should be > 3 chars")
        
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Password must be > 4 chars")
        if not self.errors:
            return True
        return False
