from animal import Animal

class dog(Animal):
    def speak(self):
        print(f"{self.name}: go go go")
        
dog = dog("husky")
dog.speak()