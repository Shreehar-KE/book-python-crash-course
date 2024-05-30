"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator's set of
privileges. Create an instance of Admin, and call your method.
"""


class User:
    """Object oriented model of a user"""

    def __init__(self, first_name, last_name, age, occupation):
        """initializes the attributes of User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        """prints the description of the user"""
        print(f'{self.first_name} {self.last_name} is {self.age} years old.')
        job = self.occupation
        if job[0] == 'a' or job[0] == 'e' or job[0] == 'i' or job[0] == 'o' or job[0] == 'u':
            print(f"{self.first_name} is an {self.occupation}\n")
        else:
            print(f"{self.first_name} is a {self.occupation}\n")

    def greet_user(self):
        """prints a greeting message to the user"""
        print(f'Hi {self.first_name}, How you doing...\n')

    def increment_login_attempts(self):
        """increments the login_attempts value by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets the login_attempts value to 0"""
        self.login_attempts = 0


class Admin(User):
    """Object Oriented representation of an Admin user"""

    def __init__(self, first_name, last_name, age, occupation):
        """initialized the attributes of Admin class"""
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = ['can add post', 'can delete post',
                           'can ban user', 'can delete user']

    def show_privileges(self):
        """displys the list of privileges that the Admin have"""
        print("The Admin's privileges are: ")
        for privilege in self.privileges:
            print(f'  - {privilege}')


admin = Admin('Admin', '', 0, 'Administrator')
admin.describe_user()
admin.show_privileges()
