class UserFinderSpy:
    def __init__(self):
        self.find_user_params = {}

    def find_user(self, first_name: str) -> dict:
        self.find_user_params["first_name"] = first_name
        return {
            "type": "user",
            "count": 1,
            "attributes": [
                {"first_name": "John", "last_name": "Doe", "age": 30, "id": "1"}
            ],
        }
