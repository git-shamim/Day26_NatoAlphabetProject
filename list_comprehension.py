numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Peterson"
letters = [letter for letter in name]
print(letters)

twice_values = [i*2 for i in range(1, 5)]
print(twice_values)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
cap_names = [name.upper() for name in names if len(name) >= 5]
print(cap_names)