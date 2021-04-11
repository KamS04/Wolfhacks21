from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.label import Label

class SpecialLabel(Label):
    pass

class FoodInfoScreen(Screen):
    harvest_time = StringProperty('')
    medicine_grid = ObjectProperty()
    sustain_grid = ObjectProperty()
    nutrition_grid = ObjectProperty()
    growth_grid = ObjectProperty()
    min_height = NumericProperty(80)

    def clear_grids(self):
        grids = [
            self.medicine_grid,
            self.sustain_grid,
            self.nutrition_grid,
            self.growth_grid
        ]

        for grid in grids:
            childs = []
            for child in grid.children:
                childs.append(child)
            for c in childs:
                grid.remove_widget(c)

    def set_food(self, food):
        self.harvest_time = food.harvest_time
        self.clear_grids()
        font_size = 14
        for data in food.growth_info:
            self.growth_grid.add_widget(SpecialLabel(text=data, font_size=font_size))
        
        for data in food.sustainability_info:
            self.sustain_grid.add_widget(SpecialLabel(text=data, font_size=font_size))
        
        for data in food.nutrition_info:
            self.nutrition_grid.add_widget(SpecialLabel(text=data, font_size=font_size))
        
        for data in food.medicinal_info:
            self.medicine_grid.add_widget(SpecialLabel(text=data, font_size=font_size))

