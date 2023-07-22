from src.infra.database.entities.users import UserModel

from pydantic import BaseModel, ConfigDict, EmailStr, StrictStr, conint, constr


class UserConfig(BaseModel):
    class Config:
        model_config = ConfigDict(extra="forbid")
        orm_model = UserModel
        orm_mode = True


class User(UserConfig):
    id: int = None
    first_name: constr(strip_whitespace=True, strict=True, min_length=2, max_length=50)
    last_name: constr(strip_whitespace=True, strict=True, min_length=2, max_length=50)
    age: conint(gt=0, lt=150)
    email: EmailStr


# class Users:
#     def __init__(self, user: User) -> None:
#         self.user = user
