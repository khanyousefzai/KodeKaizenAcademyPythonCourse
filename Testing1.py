

class Testing1:

    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password

    # getter method
    def get_first_name(self):
        return self._first_name

    # setter method
    def set_first_name(self, first_name):
        self._first_name = first_name

    # getter method
    def get_last_name(self):
        return self._last_name

    # setter method
    def set_last_name(self, last_name):
        self._last_name = last_name

    # getter method
    def get_username(self):
        return self._username

    # setter method
    def set_username(self, username):
        self._username = username

    # getter method
    def get_password(self):
        return self._password

    # setter method
    def set_password(self, password):
        self._password = password

    def __str__(self):
        return f"The user has username: {self._username} and password: {self._password}" \
               f" and first name : {self._first_name} and last name: {self._last_name} "


if __name__ == '__main__':
    u1 = Testing1('Testing1', 'Testing1', 'kodekaizenacademy@gmail.com', '1234')
    print(u1)