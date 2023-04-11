"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def get_byte_format(origin_words):
    for word in origin_words:
        byte_format_word = word.encode('UTF-8')
        str_format_word = byte_format_word.decode('UTF-8')
        print(f'Слово \'{word}\', в байтовом формате: {byte_format_word}')
        print(f'Слово \'{byte_format_word}\', в cnhjrjdjv формате: {str_format_word}')


words = ['разработка', 'администрирование', 'protocol', 'standard']
get_byte_format(words)

