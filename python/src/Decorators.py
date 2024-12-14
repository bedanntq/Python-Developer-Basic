def hello(func):
    def inner():
        print("hello")
        func()
    return inner

def name():
    print("Quunh")
    
obj = hello(name)

obj()