from src.data.use_cases.user_register import UserRegister
from src.infra.database.repositories.users_repository import UsersRepository
from src.presentation.controllers.user_register_controller import UserRegisterController


def user_resgiter_composer():
    repository = UsersRepository()
    use_case = UserRegister(repository)
    controller = UserRegisterController(use_case)

    return controller.handle
