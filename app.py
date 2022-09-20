# Прокофьев Андрей ФТ-210008
# Домашнее задание по прикладному программированию за 11 сентября

import argparse
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Шифрование и расшифровка текста шифром Цезаря.')

    parser.add_argument('-s', '--step', type=int, default=-1, help="сдвиг букв по шифру")
    parser.add_argument('-t', '--text', type=str, default="Hello world!", help="сам текст")
    parser.add_argument('-i', '--input', type=str, help="Откуда брать текст")
    parser.add_argument('-o', '--output', type=str, help="Куда отправлять результат")

    args = parser.parse_args()

    if not args.step:
        args.step = int(input("Введите шаг >> "))

    if not args.text:
        if args.input:
            with open(args.input, "r", encoding="utf-8") as file:
                args.text = file.read()
        else: 
            args.text = input("Введите текст >> ")

    result = get_caesar(args.text)

    if args.output:
        with open(args.output, "w+", encoding="utf-8") as file:
            file.write(result)
            print("Ваш результат записан в указанном файле:", args.output)
    else:
        print("Ваш результат:", result)
