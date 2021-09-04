import unittest

from distributions import SourcesLoader

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


    
if __name__ == '__main__':
    unittest.main()