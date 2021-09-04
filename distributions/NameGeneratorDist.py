from random import randrange

class NameGenerator:
    first_names = []
    last_names = []

    def __init__(self, first_names, last_names):
        self.first_names = first_names
        self.last_names = last_names

    def get_new_fname(self):
        rg_key = randrange(len(self.first_names))
        return self.first_names[rg_key]

    def get_new_lname(self):
        rg_key = randrange(len(self.last_names))
        return self.last_names[rg_key]