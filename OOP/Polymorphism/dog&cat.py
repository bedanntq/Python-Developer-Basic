from animal import Animal

class dog(Animal):
    def speak(self):
        print(f"{self.name}: go go go")
        
class cat(Animal):
    def speak(self):
        print(f"{self.name}: meo meo")

# cat = cat("kitti")
# cat.speak()
# dog = dog("husky")
# dog.speak()
animal = [dog("husky"), cat("kitti")]

for animal in animal:
    animal.speak()
