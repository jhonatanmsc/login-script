
class User:

    instance = None

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_instance(login=None, password=None):
        if not User.instance:
            if login and password:
                User.instance = User(login=login, password=password)
                return User.instance
            else:
                return False
        else:
            return User.instance

    def __str__(self):
        json = {"login":self.login,"password":self.password}
        return json