class human:
    def __init__(self, name):
        self.__name = name
    
    def profile(self):
        return self.__name
    

person = human("Quunh")
# person.__name #AttributeError: 'human' object has no attribute '__name'
print(person.profile())