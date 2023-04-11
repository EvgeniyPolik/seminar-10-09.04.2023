"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def get_byte_format(origin_words):

    for word in origin_words:
        byte_format_word = bytes(word, 'UTF-8')
        type_of_variable = type(byte_format_word)
        lenght_word_in_bytes = len(byte_format_word)
        print(f'Слово \'{word}\', в байтовом формате: {byte_format_word}, '
              f'тип переменной с кодовыми точками: {type_of_variable}, длина: {lenght_word_in_bytes}')


words = ['class', 'function', 'method']
get_byte_format(words)
