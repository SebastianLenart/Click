class User:
    def __init__(self, name):
        self.name = name

adam = User("Adam")
print(adam.name)

x = getattr(adam, "name")
print(x)

def my_func(fild_name):
    adam = User("Adamek")
    return getattr(adam, fild_name)
print(my_func("name"))