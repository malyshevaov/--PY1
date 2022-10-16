list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = 0
max_number = list_numbers [index]
for i,current_number in enumerate(list_numbers):
   max_number = list_numbers[index]
   if current_number > max_number:
      index = i
      max_number = list_numbers [index]

last_element = list_numbers[len(list_numbers) - 1]
list_numbers [len(list_numbers)-1] = max_number
list_numbers[index] = last_element

print(list_numbers)
