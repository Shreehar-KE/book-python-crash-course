"""A class that can be used to represent an Admin"""

from user import User


class Admin(User):
    """Object Oriented representation of an Admin user"""

    def __init__(self, first_name, last_name, age, occupation):
        """initialized the attributes of Admin class"""
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = Privileges(
            ['can add post', 'can delete post', 'can ban user', 'can delete user'])

    def show_privileges(self):
        """displys the list of privileges that the Admin have"""
        print("The Admin's privileges are: ")
        self.privileges.show_privileges()


class Privileges:
    """Object oriented representation of list of privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'  - {privilege}')
