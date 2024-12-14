class Human:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work
    
    def profile(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. Now, I a {self.work}")