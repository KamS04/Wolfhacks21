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
    _initialized = False
    _context = None

    def setup_grid(self, foods):
        self.clear_grid()
        for food in foods:
            view = FoodView(food)
            self.grid.add_widget(view)

    def clear_grid(self):
        childs = [c for c in self.grid.children]
        for child in childs:
            self.grid.remove_widget(child)

    def initialize(self, context):
        if not self._initialized:
            self._context = context
            foods = context.get_food_objects()
            self.setup_grid(foods)
            self.initialized = True

    def order(self, order_by):
        foods = self._context.re_sort_foods(order_by)
        self.setup_grid(foods)