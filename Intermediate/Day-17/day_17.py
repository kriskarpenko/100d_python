class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        print("New user has been created")

user_1 = User("01", "user 1")