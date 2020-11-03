

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  #исходный список

new_list = [num + 10 for num in source_list if num % 2 == 0]

print(new_list)