from random import randrange

class DateGenerator:

    def get_month(self):
        rg_mon = randrange(1,12)
        return str(rg_mon).rjust(2, '0')

    def get_day(self):
        rg_day = randrange(1,29)
        return str(rg_day).rjust(2, '0')

    def get_year(self):
        rg_year = randrange(1960, 2025)
        return str(rg_year)

    def get_new_date(self):
        return self.get_month()+'/'+self.get_day()+'/'+self.get_year()