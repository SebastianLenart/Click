fruits = ["lemon", "orange", "apple", "peach"]
print(sorted(fruits, key=len))

length = [len(fruit) for fruit in fruits]
print(length)

length2 = map(len, fruits)
print(list(length2))
print("*" * 10)


def odpocznij(name):
    print(f"{name} odpocznij")


def do_something(name, func):
    print("do_something")
    func(name)


do_something("Seba", odpocznij)
