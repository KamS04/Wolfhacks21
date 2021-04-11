import context
import gui

class Application(context.Context):
    def __init__(self):
        super().__init__()
        # Here shall be the code that initializes global variables
        pass

    def run(self):
        # Here shall be where we start the app
        # print("HELLO THERE")
        # print("General Kenobi")
        app = gui.MainApp(self)
        app.run()        

if __name__ == '__main__':
    application = Application()
    application.run()