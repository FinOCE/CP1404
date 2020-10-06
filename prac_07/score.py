from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Score Calculator"
        self.root = Builder.load_file("score.kv")
        Window.size = (400, 150)
        return self.root
    
    def handle_calculation(self, value):
        if self.test_value(value):
            value = int(value)
            if value < 0 or value > 100:
                self.root.ids.output_label.text = 'Invalid score'
            else:
                if value < 50:
                    score = 'Fail'
                elif value < 65:
                    score = 'Pass'
                elif value < 75:
                    score = 'Credit'
                elif value < 85:
                    score = 'Distinction'
                else:
                    score = 'High Distinction'
                self.root.ids.output_label.text = score
    
    def test_value(self, value):
        try:
            value = int(value)
            return True
        except ValueError:
            self.root.ids.output_label.text = 'Invalid score'
            return False
    
    def clear_fields(self):
        self.root.ids.output_label.text = "Enter your score"
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
