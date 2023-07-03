from pydantic import BaseModel, ConfigDict, EmailStr, conint, constr


class User(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    first_name: constr(strip_whitespace=True, strict=True, min_length=2, max_length=50)
    last_name: constr(strip_whitespace=True, strict=True, min_length=2, max_length=50)
    age: conint(gt=0, lt=150)
    email: EmailStr


class Users:
    def __init__(self, user: User) -> None:
        self.user = user
