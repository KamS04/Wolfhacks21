import os
import data

class Constants():
    def __init__(self, data):
        self.data = data

    def __getattr__(self, name: str):
        #print(name, self.data)
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
    # Sortings Enum
    'NAME': lambda food: food.name,
    'GROWTH': lambda food: food.growth,
    'NUTRITION': lambda food: food.nutrition,
    'HARVEST': lambda food: food.harvest,
    'SUSTAINABILITY': lambda food: food.sustainability,
    'MEDICINAL': lambda food: food.medicinal,
}

FILES = {
    'imgs': Constants ( {
        'homescreen_bg': os.path.join('rootdir', 'assets', 'imgs', 'homescreenbg.png'),
        'avatar': os.path.join('rootdir', 'assets', 'imgs', 'avatar.png'),
        'stars': os.path.join('rootdir', 'assets', 'imgs', 'stars.png'),
        'food': os.path.join('rootdir', 'assets', 'imgs', 'food.jpg'),
        'amaranth': os.path.join('rootdir', 'assets', 'imgs', 'amaranth.png'),
        'ginger': os.path.join('rootdir', 'assets', 'imgs', 'ginger.png'),
        'potatoes': os.path.join('rootdir', 'assets', 'imgs', 'potatoes.png'),
        'spinach': os.path.join('rootdir', 'assets', 'imgs', 'spinach.png'),
        'strawberry': os.path.join('rootdir', 'assets', 'imgs', 'strawberry.png'),
        'wheat': os.path.join('rootdir', 'assets', 'imgs', 'wheat.png'),
        'asparagus': os.path.join('rootdir', 'assets', 'imgs', 'asparagus.png'),
        'barley': os.path.join('rootdir', 'assets', 'imgs', 'barley.png'),
        'basil': os.path.join('rootdir', 'assets', 'imgs', 'basil.png'),
        'beetroot': os.path.join('rootdir', 'assets', 'imgs', 'beetroot.png'),
    }),
    'kv_files': [
        os.path.join('rootdir', 'assets', 'kv_files', 'homescreen.kv'),
        os.path.join('rootdir', 'assets', 'kv_files', 'passengersscreen.kv'),
        os.path.join('rootdir', 'assets', 'kv_files', 'foodscreen.kv'),
        os.path.join('rootdir', 'assets', 'kv_files', 'foodinfoscreen.kv')
    ],
    'app_kv': os.path.join('rootdir', 'assets', 'main.kv')
}

COLORS = {
    'primary': Constants( {
        'primary': '#0d47a1',
        'light': '#5472d3'
    })
}


class Context():
    def __init__(self):
        # initialize database here
        self.constants = Constants(CONSTANTS)
        self.files = Constants(FILES)
        self.colors = Constants(COLORS)
        self.initialize_database()
    
    def initialize_database(self):        
        # INIT Foods
        foods = data.gen_foods(self)
        # sort foods
        self.foods = sorted(foods, key=self.constants.NAME)
    
    def get_file(self, file_path):
        f = file_path.replace('rootdir', os.path.dirname(__file__))
        return f
    
    def re_sort_foods(self, sort_name):        
        self.foods = sorted(self.foods, key=self.constants[sort_name])
        return self.foods

    def get_food_objects(self):
        return self.foods