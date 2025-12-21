class AuthService:
    def __init__(self):
        # Could be DB or API in real app
        self._users = {"alice": "password123", "bob": "qwerty"}

    def login(self, username: str, password: str) -> bool:
        """Return True if username/password match"""
        return self._users.get(username) == password

    def logout(self, username: str):
        print(f"{username} logged out")
