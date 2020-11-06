with open('text_2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for index, value in enumerate(lines, 1):
        number= len(value.split())
        print(f'{index} {number}')