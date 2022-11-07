from random import choice
def get_unique_list_numbers() -> list[int]:
    size = 15
    list_numbers = list(range(-10,11))
    new_list = []
    while len(new_list) < size:
        current = choice(list_numbers)
        if current not in new_list:
            new_list.append(current)
    return new_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
