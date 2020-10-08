from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertTemps(App):
    def build(self):
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperature.kv')
        Window.size = (200, 100)
        return self.root
    
    def convert_f_to_c(self, fahrenheit):
        if self.is_valid(fahrenheit):
            celsius = 5 / 9 * (float(fahrenheit) - 32)
            self.root.ids.output.text = f"{celsius:.3f}"
    
    def convert_c_to_f(self, celsius):
        if self.is_valid(celsius):
            fahrenheit = float(celsius) * 9 / 5 + 32
            self.root.ids.output.text = f"{fahrenheit:.3f}"
    
    def is_valid(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

ConvertTemps().run()