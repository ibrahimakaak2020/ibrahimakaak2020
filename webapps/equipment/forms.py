from typing import List
from typing import Optional

from fastapi import Request


class EquipmentCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.sn: Optional[str] = None
        self.model: Optional[str] = None
        self.location: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.sn = form.get("sn")
        self.model = form.get("model")
        self.location = form.get("location")

    async def is_valid(self):
        if not self.sn :
            self.errors.append("SN should be Not Null ...")
        if not self.model:
            self.errors.append("Model should be Not Null ...")
        
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Password must be > 4 chars")
        if not self.errors:
            return True
        return False
