# models/user_model.py
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def rename(self, new_name: str):
        self.name = new_name
