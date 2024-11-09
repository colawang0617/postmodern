class PasswordMatcher:
    owner_password = None
    PASSWORD_LENGTH = 5

    def __init__(self):
        self.owner_password = '10158'  # placeholder temporary password, will be read from database

    def is_owner_password(self, password):
        return password == self.owner_password
