def my_func(a, b, c):
    print(a)
    print(b)
    print(c)


data = {"a": 1, "c": 2, "b": 3} # inna kolejnosc ale potem sie dopasuje a-a, b-b, c-c
my_func(**data)
