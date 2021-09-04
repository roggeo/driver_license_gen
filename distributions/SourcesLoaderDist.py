import os

class SourcesLoader:

    def read_file(self, file_name):
        file_txt = open(os.path.dirname(os.path.abspath(__file__))+'/'+file_name)
        f_read = file_txt.readlines()
        file_txt.close()
        return f_read

    def get_list_names(self, file_name):
        list_names = self.read_file(file_name)
        return [s.strip() for s in list_names]

    def get_first_names(self):
        return self.get_list_names('first_names.txt')

    def get_last_names(self):
        return self.get_list_names('last_names.txt')