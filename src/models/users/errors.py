class UserErrors(Exception):
    def __int__(self, message):
        self.message=message


class UserDoesntExist(UserErrors):
    pass


class UserAlreadyRegistered(UserErrors):
    pass


class PasswordIncorrect(UserErrors):
    pass
