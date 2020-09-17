class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year
    
    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False
    
    def __str__(self):
        # return f"{self.language}, {self.typing} Typing, Reflection={self.is_dynamic()}, First appeared in {self.year}"
        return self.language