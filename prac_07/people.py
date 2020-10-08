from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import StringProperty

class People(App):
    output = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = self.get_people()
    
    def build(self):
        self.title = 'People'
        self.root = Builder.load_file('people.kv')
        Window.size = (400, 200)
        self.create_widgets()
        return self.root
    
    def create_widgets(self):
        for row in self.rows:
            temp_button = Button(text=row)
            temp_button.bind(on_press=self.display_age)
            self.root.ids.widgets_box.add_widget(temp_button)
    
    def get_people(self):
        file = open('prac_07/people.csv', 'r')
        rows_raw = [row for row in file]
        file.close()

        rows = {}
        for row in rows_raw:
            row_content = row.strip().split(',')
            row_content[1] = int(row_content[1])
            rows[row_content[0]] = row_content[1]
        return rows
    
    def display_age(self, instance):
        self.output = f"Name: {instance.text} | Age: {self.rows[instance.text]}"

People().run()