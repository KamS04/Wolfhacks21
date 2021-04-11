import kivy
from kivy.app import App
from kivy.lang.builder import Builder

# widgets
from ui import homescreen

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

