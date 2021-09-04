from random import randrange

class ClassLicenseGenerator:

    classes = ['M','A','B','C'];

    def get_new_class(self):
        return self.classes[randrange(len(self.classes))]