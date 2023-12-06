"""A class that can be used to represent priveleges"""


class Priveleges:
    """Object oriented representation of list of priveleges"""

    def __init__(self, priveleges):
        self.priveleges = priveleges

    def show_priveleges(self):
        for privelege in self.priveleges:
            print(f'  - {privelege}')
