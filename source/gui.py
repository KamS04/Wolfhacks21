import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import SlideTransition

# widgets
from ui import homescreen, passengersscreen, foodscreen, food_info

def calculate_size(width, aspect_ratio):
    height = width * aspect_ratio[1] / aspect_ratio[0]
    return width, height

ASPECT_RATIO = (1600, 987)

Window.size = calculate_size(1000, ASPECT_RATIO)

class MainApp(App):
    passengers_screen = 'passengers'
    home_screen = 'home'
    food_screen = 'food'
    
    screen_moves = {
        home_screen: 0,
        passengers_screen: 1,
        food_screen: 1,
        'food_info': 2
    }

    def __init__(self, context):
        super().__init__()
        self.context = context

    def build(self):
        for kv_file in self.context.files.kv_files:
            file = self.context.get_file(kv_file)
            Builder.load_file(file)
        
        main_kv = self.context.get_file(self.context.files.app_kv)        
        return Builder.load_file(main_kv)

    def on_start(self):
        self.food_info_screen = self.root.ids['food_info_screen']
        self.root.ids['food_screen'].initialize(self.context)

    def switch_screen(self, screen_name):
        if self.screen_moves[self.root.current] > self.screen_moves[screen_name]:
            self.root.transition = SlideTransition(direction='right')
        else:
            self.root.transition = SlideTransition(direction='left')                
        self.root.current = screen_name
    
    def show_food_info(self, food):
        self.food_info_screen.set_food(food)
        self.switch_screen(self.food_info_screen.name)

