from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("greeter.kv")
        Window.size = (400, 150)
        return self.root
    def handle_greet(self):
        print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text
    def clear_fields(self):
        print('fields cleared')
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
