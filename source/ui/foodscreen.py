from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from classes import food
from kivy.app import App

class FoodView(ButtonBehavior, FloatLayout):
    id = NumericProperty(0)
    name = StringProperty('')
    growth = NumericProperty(0)
    nutrition = NumericProperty(0)
    harvest = NumericProperty(0)
    sustainability = NumericProperty(0)
    medicinal = NumericProperty(0)
    image = StringProperty('')    

    def __init__(self, food, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = food.ID
        self.name = food.name
        self.growth = food.growth
        self.nutrition = food.nutrition
        self.harvest = food.harvest
        self.sustainability = food.sustainability
        self.medicinal = food.medicinal
        self.image = food.image
        self.food = food
    
    def on_press(self, *args):
        App.get_running_app().show_food_info(self.food)

class FoodScreen(Screen):
    grid = ObjectProperty()

    def on_kv_post(self, *args):
        for i in range(10):
            app = App.get_running_app()
            p = food.Food(i, f'Food#{i+1}', 2, 3, 1, 2, 4, app.context.get_file(app.context.files.imgs.food))
            v = FoodView(p)
            self.grid.add_widget(v)
        pass