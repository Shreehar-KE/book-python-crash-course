"""A class that can be used to represent privileges"""


class Privileges:
    """Object oriented representation of list of privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'  - {privilege}')
