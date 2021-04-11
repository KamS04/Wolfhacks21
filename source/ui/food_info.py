from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label

class FoodInfoScreen(Screen):
    harvest_time = StringProperty('')
    medicine_grid = ObjectProperty()
    sustain_grid = ObjectProperty()
    nutrition_grid = ObjectProperty()
    growth_grid = ObjectProperty()

    def clear_grids(self):
        grids = [
            self.medicine_grid,
            self.sustain_grid,
            self.nutrition_grid,
            self.growth_grid
        ]

        for grid in grids:
            for child in grid.children:
                grid.remove_widget(child)
                del child                

    def set_food(self, food):
        self.harvest_time = food.harvest_time
        self.clear_grids()
        for data in food.growth_info:
            self.growth_grid.add_widget(Label(text=data))
        
        for data in food.sustainability_info:
            self.sustain_grid.add_widget(Label(text=data))
        
        for data in food.nutrition_info:
            self.nutrition_grid.add_widget(Label(text=data))
        
        for data in food.medicinal_info:
            self.medicine_grid.add_widget(Label(text=data))                            