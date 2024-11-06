def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Получаем текущую позицию в байтах
            byte_position = file.tell()
            # Записываем строку в файл с символом новой строки
            file.write(string + '\n')
            # Сохраняем номер строки (индекс + 1) и позицию
            strings_positions[(index + 1, byte_position)] = string

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
