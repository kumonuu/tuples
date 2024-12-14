fruits = ("apple", "orange", "banana", ("strawberry", "raspberry"))
characters = ("a", "d", "o", "g", "i")
fruit1, fruit2, fruit3, fruit4 = fruits
print(fruits)
print(fruits[1])
# fruits[1] = "blueberry"

for fruit in fruits:
    print(fruit)

print(fruit1)
print(fruit2)

print(fruits[3][1])
print(characters[1:4])
print(characters[1:])
print(characters[0:])