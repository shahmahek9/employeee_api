from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import models, schemas
from ..dependencies import get_db
from ..dependencies_auth import get_current_user


router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)


@router.post("/", response_model=schemas.EmployeeResponse, status_code=201)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user)
):
    ...

    # Check duplicate email
    existing = db.query(models.Employee).filter(
        models.Employee.email == employee.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Employee with this email already exists"
        )

    new_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        role=employee.role
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee
@router.get(
    "/",
    response_model=List[schemas.EmployeeResponse]
)
def list_employees(
    page: int = Query(1, ge=1),
    department: Optional[str] = None,
    role: Optional[str] = None,
    db: Session = Depends(get_db),
      _: str = Depends(get_current_user)
):
    query = db.query(models.Employee)

    if department:
        query = query.filter(models.Employee.department == department)

    if role:
        query = query.filter(models.Employee.role == role)

    page_size = 10
    offset = (page - 1) * page_size

    employees = query.offset(offset).limit(page_size).all()
    return employees
@router.get(
    "/{employee_id}",
    response_model=schemas.EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
      _: str = Depends(get_current_user)
):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee
@router.put(
    "/{employee_id}",
    response_model=schemas.EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee_update: schemas.EmployeeUpdate,
    db: Session = Depends(get_db),
      _: str = Depends(get_current_user)
):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if employee_update.name is not None:
        employee.name = employee_update.name
    if employee_update.department is not None:
        employee.department = employee_update.department
    if employee_update.role is not None:
        employee.role = employee_update.role

    db.commit()
    db.refresh(employee)

    return employee
@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
      _: str = Depends(get_current_user)
):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
from ..dependencies_auth import get_current_user
router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"],
    dependencies=[Depends(get_current_user)]
)
