CONSTANTS = {
    
}

class Constants():
    def __init__(self, data):
        self.data = data

    def __getattribute__(self, name: str):
        return self.data[name]
    
    def __getitem__(self, name):
        return self.data[name]

class Context():
    def __init__(self):
        # initialize database here
        self.constants = Constants(CONSTANTS)
        # self.database =
        pass

    def get_database(self):
        # manchits databsase goes here
        return self.database
    
    def initialize_database(self):
        # initialize connection to database here
        pass

