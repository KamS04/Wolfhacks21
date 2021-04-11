from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.app import App


class DietItem:
    def __init__(self, food, number):
        self.food = food
        self.number = number


class DietView(GridLayout):
    name = StringProperty('')
    image = StringProperty('')
    quantity = StringProperty('')

    def __init__(self, dietitem):
        super().__init__()
        self.name = dietitem.food.name
        self.image = dietitem.food.image
        self.quantity = dietitem.number


class AddItem(Widget):
    food_inp = ObjectProperty()
    quan_inp = ObjectProperty()

    def __init__(self, context, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = context
    
    def save_and_exit(self, *args):
        food = self.food_inp.text
        quantity = self.quan_inp.text
        self.context.save_item(food, quantity)


class DietScreen(Screen):
    id = NumericProperty(0)
    p_name = StringProperty('')
    height = NumericProperty(0)
    age = NumericProperty(0)
    weight = NumericProperty(0)
    image = StringProperty('')
    _cached = {}
    _diet_items = []
    diet_grid = ObjectProperty()
    _popup = None

    def set_passenger(self, passenger):
        self.id = passenger.id
        self.p_name = passenger.name
        self.height = passenger.height
        self.weight = passenger.weight
        self.image = passenger.avatar
        self.age = passenger.age
        self._diet_items = self._cached[passenger.id] if passenger.id in self._cached.keys() else []
        self.passenger = passenger
        self.setup_grid()
    
    def setup_grid(self):
        self.clear_grid()
        for meal in self._diet_items:
            view = DietView(meal)
            self.diet_grid.add_widget(view)

    def clear_grid(self):
        childs = [child for child in self.diet_grid.children]
        for child in childs:
            self.diet_grid.remove_widget(child)

    def add_item(self):
        add_view = AddItem(self)
        self._popup = Popup(title='Add', content=add_view, size_hint=(0.6, 0.8))
        self._popup.open()

    def save_item(self, food, quantity):
        self._popup.dismiss()
        food = food.lower()
        context = App.get_running_app().context
        foods = context.get_food_objects()
        food_names = [food.name.lower() for food in foods]
        print(food_names)
        if food in food_names:
            sfood = next(sfood for sfood in foods if sfood.name.lower() == food)
            diet_item = DietItem(sfood, quantity)
            self._diet_items = [diet_item] + self._diet_items
            self._cached[self.passenger.id] = self._diet_items
            self.setup_grid()