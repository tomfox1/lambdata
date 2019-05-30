class Cake: 
    """example"""
    x=2

    def __init__(self):
        self.baked = False

    def bake(self):
        self.baked = True
        print("All done!")

class Datacleaner: 
    """"class for cleaning our data"""

    def __init__(self, df):
        self.df = df
    def replace_values(self, value=np.nan, new=0):
        """replace values in a dataframe""" 
        self.df = self.df.replace(value, new)
    def impute_values(self):
        pass


