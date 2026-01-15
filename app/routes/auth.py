from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "supersecretkey"   # move to env in real projects
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
from fastapi import APIRouter, HTTPException
from datetime import timedelta
from ..auth import create_access_token, get_password_hash, verify_password

router = APIRouter(tags=["Auth"])

# Hardcoded demo user
fake_user = {
    "username": "admin",
    "hashed_password": None
}

fake_user["hashed_password"] = get_password_hash("admin123")


@router.post("/api/token")
def login(username: str, password: str):
    if username != fake_user["username"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, fake_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": token, "token_type": "bearer"}
