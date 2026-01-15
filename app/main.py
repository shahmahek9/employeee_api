from fastapi import FastAPI
from app.database import Base, engine
from app.routes import employees, auth

app = FastAPI(title="Employee Management API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(employees.router)

@app.get("/")
def health():
    return {"status": "ok"}
