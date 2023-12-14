from fileio import FileIO
import json

users = [{
    'username': "ahmet",
    'password': "12345"
}]


class Auth:
    file_name = 'user.txt'

    def __init__(self):
        self.users = json.loads(FileIO(self.file_name).read())
        self.__username = None
        print(self.users)
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        print("username is private")

    
    def login_or_signup(self, username):
        username_index = -1
        for index, user in enumerate(self.users):
            if user["username"] == username:
                username_index = index
        
        if username_index > -1:
            password = input("Enter your password to login: ")
        else:
            password = input("Enter your password to signup: ") 

        if username_index > -1:
            if self.users[username_index]["password"] == password:
                self.username = username
            else:
                print("Please check your username and password")
        else:
            self.users.append({
                "username": username,
                "password": password
            })
            self.username = username

    def signout(self):
        self.username = None

    def __del__(self):
        print("delete Auth")
        json_users = json.dumps(self.users)
        FileIO(self.file_name).write(json_users)

