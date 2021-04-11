from re import X
import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

# widgets
from ui import homescreen

def calculate_size(width, aspect_ratio):
    height = width * aspect_ratio[1] / aspect_ratio[0]
    return width, height

ASPECT_RATIO = (1600, 987)

Window.size = calculate_size(1000, ASPECT_RATIO)

class MainApp(App):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def build(self):
        for kv_file in self.context.files.kv_files:
            file = self.context.get_file(kv_file)
            Builder.load_file(file)
        
        main_kv = self.context.get_file(self.context.files.app_kv)        
        return Builder.load_file(main_kv)

