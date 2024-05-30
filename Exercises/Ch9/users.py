"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user's information. Make another method called greet_user() that prints
a personalized greeting to the user.
    
     Create several instances representing different users, and call both methods 
for each user.
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


chandler = User('Chandler', 'Bing', 26,
                'Statistical Analysis and Data Reconfiguration')
joey = User('Joey', 'Tribbiani', 25, 'Actor')
phoebe = User('Phoebe', 'Buffay', 26, 'Masseuse')
ross = User('Ross', 'Geller', 26, 'Palaeontologist')
rachel = User('Rachel', 'Green', 24, 'Waitress')
monica = User('Monica', 'Geller', 24, 'Chef')

chandler.describe_user()
chandler.greet_user()
joey.describe_user()
joey.greet_user()
phoebe.describe_user()
phoebe.greet_user()
ross.describe_user()
ross.greet_user()
rachel.describe_user()
rachel.greet_user()
monica.describe_user()
monica.greet_user()
