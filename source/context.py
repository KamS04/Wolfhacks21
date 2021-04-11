import os


class Constants():
    def __init__(self, data):
        self.data = data

    def __getattr__(self, name: str):
        print(name, self.data)
        return self.data[name]
    
    def __getitem__(self, name):
        return self.data[name]

    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]
    
    def __contains__(self, key):
        return key in self.data

    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)


CONSTANTS = {

}

FILES = {
    'imgs': Constants ( {
        'homescreen_bg': r'rootdir\assets\imgs\homescreenbg.png'
    }),
    'kv_files': [
        r'rootdir\assets\kv_files\homescreen.kv'
    ],
    'app_kv': r'rootdir\assets\main.kv'
}

class Context():
    def __init__(self):
        # initialize database here
        self.constants = Constants(CONSTANTS)
        self.files = Constants(FILES)
        # self.database =
        pass

    def get_database(self):
        # manchits databsase goes here
        return self.database
    
    def initialize_database(self):
        # initialize connection to database here
        pass
    
    def get_file(self, file_path):
        f = file_path.replace('rootdir', os.path.dirname(__file__))
        return f