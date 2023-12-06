"""A class that can be used to represent an Admin"""

from user import User
from privileges import Priveleges


class Admin(User):
    """Object Oriented representation of an Admin user"""

    def __init__(self, first_name, last_name, age, occupation):
        """initialized the attributes of Admin class"""
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = Priveleges(
            ['can add post', 'can delete post', 'can ban user', 'can delete user'])

    def show_privileges(self):
        """displys the list of privileges that the Admin have"""
        print("The Admin's privileges are: ")
        self.privileges.show_priveleges()
