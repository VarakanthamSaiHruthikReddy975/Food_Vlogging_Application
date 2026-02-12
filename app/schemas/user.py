from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 10:
            raise("Password must be at least 10 characters")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Must contain an uppercase letter")
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Must contain special character")
    
        return value