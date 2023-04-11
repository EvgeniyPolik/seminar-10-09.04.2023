"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def get_byte_format(origin_words):
    for word in origin_words:
        byte_format_word = bytes(word, 'UTF-8')
        type_of_variable = type(byte_format_word)
        lenght_word_in_bytes = len(byte_format_word)

        try:
            if lenght_word_in_bytes != len(word):
                raise ValueError
        except ValueError:
            print(f'Слово: \'{word}\' не может быть записать в байтовом типе с помощью маркировки b\'\' '
                  f'(без encode decode).')
        else:
            print(f'Слово \'{word}\', в байтовом формате: {byte_format_word}, '
                  f'тип переменной с кодовыми точками: {type_of_variable}, длина: {lenght_word_in_bytes}')


words = ['attribute', 'класс', 'функция', 'type']
get_byte_format(words)
