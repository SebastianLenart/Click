def say_hello(first_name="Kacper"):
    return f"hello {first_name}"


say_hello2 = lambda first_name="domslna": f"hello {first_name}"  # po : zawsze jest return

# lambda uzywamy kiedy chcemy przekazac funkcje jako argument

say_hello_to_kacper = say_hello()
say_hello_to_kacper2 = say_hello2()

print(say_hello_to_kacper)
print(say_hello_to_kacper2)
print("*" * 10)


def starts_with_a(name):
    return name[0].lower() == "a"


names = ["Adam", "Alina", "Seba"]
names_starts_with_a = filter(starts_with_a, names)
names_starts_with_a2 = filter(lambda name: name[0].lower() == "a", names)
print(list(names_starts_with_a))
print(list(names_starts_with_a2))
print("*" * 10)

# inne przyklady to map i sort

calc = {
    "odejmij": lambda a, b: a-b
}
funtion = calc["odejmij"]
funtion2 = calc["odejmij"](2, 2)
print(funtion(1, 2))
print(funtion2) # dziala tez