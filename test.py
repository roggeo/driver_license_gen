import unittest

from distributions import SourcesLoader
from distributions import NameGenerator
from distributions import DateGenerator

class TestSourcesLoaderClass(unittest.TestCase):
    
    def setUp(self):
        self.loader = SourcesLoader()
        self.first_names = self.loader.get_first_names()
        self.last_names = self.loader.get_last_names()
        pass

    def test_read_names(self): 
        for name in self.first_names:
            self.assertEqual(len(name) >= 3, True, name +' is not a valid first name')
        pass

    def test_read_last_names(self): 
        for name in self.last_names:
            self.assertEqual(len(name) >= 3, True, name +' is not a valid last name')
        pass


class TestNameGeneratorClass(unittest.TestCase):

    def setUp(self):
        self.loader = SourcesLoader()
        self.first_names = self.loader.get_first_names()
        self.last_names = self.loader.get_last_names()

        self.generator = NameGenerator(self.first_names, self.last_names)

    def test_generate_first_name(self):
        new_name = self.generator.get_new_fname()
        self.assertEqual(len(new_name) >= 3, True, new_name +' is not a valid first name')

    def test_generate_last_name(self):
        new_name = self.generator.get_new_lname()
        self.assertEqual(len(new_name) >= 3, True, new_name +' is not a valid last name')
    


class TestDateGeneratorClass(unittest.TestCase):

    def setUp(self):
        self.generator = DateGenerator()
        
    def test_new_date(self):
        new_date = self.generator.get_new_date()
        self.assertEqual(len(new_date) == 10, True, 'date is not valid')


if __name__ == '__main__':
    unittest.main()