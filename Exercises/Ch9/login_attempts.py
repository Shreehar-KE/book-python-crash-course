class User:
    """Object oriented model of a user"""

    def __init__(self, first_name, last_name, age, occupation):
        """initializes the attributes of User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

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


heisenberg = User('Walter', 'White', 50, 'Chemistry Teacher')
heisenberg.increment_login_attempts()
print(heisenberg.login_attempts)
heisenberg.reset_login_attempts()
print(heisenberg.login_attempts)
