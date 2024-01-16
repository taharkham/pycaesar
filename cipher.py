#Комментарий от taharkh@m

# Методы для реализации шифра Цезаря

import string

value_list = list(string.digits)
eng_lower_list = list(string.ascii_lowercase)
eng_upper_list = list(string.ascii_uppercase)
rus_lower_list = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
rus_upper_list = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")


class LengthError(Exception):
    """
    Тип ошибки для отладки скрипта шифра.
    """


def rotate_letter(letter, rotate, letter_list):
    """
    Найти букву по принципу шифра Цезаря
    """
    letter_pos = letter_list.index(letter) + rotate
    list_len = len(letter_list)
    letter_pos %= list_len
    return letter_list[letter_pos]


def get_caesar(text: str, rotate: int):
    """
    Зашифровать текст по шифру Цезаря
    """

    if len(text) == 0:
        raise LengthError("Введённая строка пуста (длина равна нулю)")

    response = ""

    for i in list(text):
        if i in value_list:
            r = rotate_letter(i, rotate, value_list)

        elif i in eng_lower_list:
            r = rotate_letter(i, rotate, eng_lower_list)

        elif i in eng_upper_list:
            r = rotate_letter(i, rotate, eng_upper_list)

        elif i in rus_lower_list:
            r = rotate_letter(i, rotate, rus_lower_list)

        elif i in rus_upper_list:
            r = rotate_letter(i, rotate, rus_upper_list)

        else:
            r = i
        
        response += r

    return response
