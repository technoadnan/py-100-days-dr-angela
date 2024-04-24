numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]


name = "Angela"
letters_list = [letter for letter in name]
range_list = [num * 2 for num in range(1,5)]
names = ["ALex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']


short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]


# Add spaces between the elements of the list
new_names = [name + " " for name in names]

# Print the modified list
print(new_names)