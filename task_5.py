"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

def get_ping(destination_adresses):
    for address in destination_adresses:
        print(f'Проверка до узла: {address}')
        command = ['ping']
        command.append(address)
        do_ping = subprocess.Popen(command, stdout=subprocess.PIPE)
        for line in do_ping.stdout:
            line_encode = chardet.detect(line)
            print(line.decode(line_encode['encoding']).strip())

addresses = ['yandex.ru', 'youtube.com']
get_ping(addresses)
