class CalcDigit:
    def calculate(self, df, ds):
        return df - ds


# incorrect
class SubsDigit(CalcDigit):
    def calculate(self, df, ds):
        return df - ds


# correct

class AddDigit(CalcDigit):
    def calculate(self, df, ds):
        return ds + df
