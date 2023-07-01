from pydantic import BaseModel, EmailStr, Extra, conint, constr


class CustomBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid


class User(CustomBaseModel):
    id: int
    first_name: constr(
        strip_whitespace=True, strict=True, min_length=2, curtail_length=50
    )
    last_name: constr(
        strip_whitespace=True, strict=True, min_length=2, curtail_length=50
    )
    age: conint(gt=0, lt=150)
    email: EmailStr


class Users:
    def __init__(self, user: User) -> None:
        self.user = user
