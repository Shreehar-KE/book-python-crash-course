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


class Privileges:
    """Object oriented representation of list of privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'  - {privilege}')


class Admin(User):
    """Object Oriented representation of an Admin user"""

    def __init__(self, first_name, last_name, age, occupation):
        """initialized the attributes of Admin class"""
        super().__init__(first_name, last_name, age, occupation)
        # self.privileges = ['can add post', 'can delete post',
        #                    'can ban user', 'can delete user']
        self.privileges = Privileges(
            ['can add post', 'can delete post', 'can ban user', 'can delete user'])

    def show_privileges(self):
        """displys the list of privileges that the Admin have"""
        print("The Admin's privileges are: ")
        # for privilege in self.privileges:
        #     print(f'  - {privilege}')
        self.privileges.show_privileges()


admin = Admin('Admin', '', 0, 'Administrator')
admin.describe_user()
admin.show_privileges()
