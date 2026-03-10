from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.security.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


# Demo user
fake_user = {
    "username": "admin",
    "password": "$2b$12$GoktS6IBNkQiomkt73IfxeHSUa3sSqBgTLG20HUrTp5c8Ld.urIPG"
}
# password = 123456


@router.post("/login")
def login(data: LoginRequest):
    """
    API login trả về JWT token
    """

    if data.username != fake_user["username"]:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not verify_password(data.password, fake_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }