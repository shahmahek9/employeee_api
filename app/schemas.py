from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str] = None
    role: Optional[str] = None
class EmployeeCreate(EmployeeBase):
    pass
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    role: Optional[str] = None
class EmployeeResponse(EmployeeBase):
    id: int
    date_joined: date

    class Config:
        from_attributes = True
