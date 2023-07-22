class UserRegisterSpy:
    def __init__(self) -> None:
        self.params = {}

    def register_user(self, params: dict) -> None:
        return {"statatus_code": 200, "body": {**params}}
