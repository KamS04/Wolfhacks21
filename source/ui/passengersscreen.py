from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from classes import passenger
from kivy.app import App

class PassengerView(ButtonBehavior, FloatLayout):
    id = NumericProperty(0)
    name = StringProperty('')
    height = NumericProperty(0)
    age = NumericProperty(0)
    weight = NumericProperty(0)
    image = StringProperty('')

    def __init__(self, passenger, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = passenger.id
        self.age = passenger.age
        self.height = passenger.height
        self.weight = passenger.weight
        self.image = passenger.avatar
        self.name = passenger.name
        self.passenger = passenger
    
    def on_press(self, *args):
        App.get_running_app().show_diet_screen(self.passenger)


class PassengersScreen(Screen):
    grid = ObjectProperty()    

    def on_kv_post(self, *args):
        for i in range(10):
            p = passenger.Passenger(i, f'{i+1}', 12, 176, 120, App.get_running_app().context.files.imgs.avatar)
            v = PassengerView(p)
            self.grid.add_widget(v)