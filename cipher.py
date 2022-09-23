# Методы для реализации шифра Цезаря

import string

value_list = list(string.hexdigits)
eng_lower_list = list(string.ascii_lowercase)
eng_upper_list = list(string.ascii_uppercase)
rus_lower_list = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
rus_upper_list = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

def rotate_letter():
    # закончить вставку
    return ""

def get_caesar(text: str, rotate: int):
    if len(text) != 0:
        raise Exception("Введённая строка пуста (длина равна нулю)")
    response = ""

    for i in list(text):
        print(i, sep=" ")
        # закончить вставку

    return response