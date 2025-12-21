from models.user_model import User


class UserService:
    """Simulates a database or API"""

    def get_users(self) -> list[User]:
        return [User("Alice", "alice@example.com"), User("Bob", "bob@example.com")]

    def save_user(self, user: User):
        print(f"Saving user {user.name} to database")
