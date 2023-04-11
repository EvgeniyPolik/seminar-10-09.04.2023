"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def get_code_points(origin_words):

    for word in origin_words:
        code_point_word = ascii(word)
        type_of_variable = type(code_point_word)
        print(f'Слово \'{word}\', в формате кодовых точек: {code_point_word}, '
              f'тип переменной с кодовыми точками: {type_of_variable}.')


words = ['разработка', 'сокет', 'декоратор']
get_code_points(words)
