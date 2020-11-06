with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input('Введите текст: ')
        if not text:
            break
    print(text)
