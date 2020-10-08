from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

RATIO = 1.609344

class ConvertMilesKM(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles To KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        Window.size = (200, 100)
        return self.root

    def handle_increment(self, value, increment):
        if value == '':
            self.root.ids.miles_value.text = '0'
            value = 0
        if self.test_value(value):
            if float(value).is_integer():
                value = int(value)
            else:
                value = float(value)
            
            # Defining a max decimal so the value doesn't randomly change to something like 1.200000000005
            if '.' in str(value):
                decimal_max = f".{len(str(value).split('.')[1])}f"
            else:
                decimal_max = 0
            self.root.ids.miles_value.text = f"{value + increment:{decimal_max}}"

    def handle_conversion(self, value):
        if value == '':
            self.root.ids.miles_value.text = '0'
            value = 0
        if self.test_value(value):
            km = f"{float(value) * RATIO:.3f}"
            self.root.ids.output_label.text = km

    def test_value(self, value):
        try:
            value = float(value)
            return True
        except ValueError:
            if value == '':
                return True
            else:
                return False

# create and start the App running
ConvertMilesKM().run()
