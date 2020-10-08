from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label

NAMES = ["Michael Contoso", "John Doe", "Finley Sherwood"]

class DynamicLabels(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        Window.size = (200, 100)
        self.create_widgets()
        return self.root
    
    def create_widgets(self):
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.widgets_box.add_widget(temp_label)

# create and start the App running
DynamicLabels().run()