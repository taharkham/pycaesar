# Прокофьев Андрей ФТ-210008
# Домашнее задание по прикладному программированию за 25 сентября

import argparse
from cipher import get_caesar

def main():
    """
    Запуск скрипта через функцию для импорта
    """

    # Парсинг команды cmd/bash
    parser = argparse.ArgumentParser(description='Шифрование и расшифровка текста шифром Цезаря.')

    parser.add_argument('-s', '--step', type=int, help="сдвиг букв по шифру")
    parser.add_argument('-t', '--text', type=str, help="сам текст")
    parser.add_argument('-i', '--input', type=str, help="Откуда брать текст")
    parser.add_argument('-o', '--output', type=str, help="Куда отправлять результат")

    args = parser.parse_args()

    # обработка аргументов к команде
    # Количество шагов по смещению буквы
    if not args.step:
        while True:
            try:
                args.step = int(input("Введите шаг >> "))
                
            except Exception as e:
                print("Ошибка:", e)

            finally:
                break
        
    # Текст для шифрования
    if not args.text:
        if args.input:
            with open(args.input, "r", encoding="utf-8") as file:
                args.text = file.read()

        else: 
            while True:
                args.text = input("Введите текст >> ")

                if args.text == "":
                    print("Ошибка: нельзя вставлять пустой текст")
                    continue

                break

    # Шифровка
    result = get_caesar(args.text, args.step)

    # Печать результата в консоль/файл
    if args.output:
        with open(args.output, "w+", encoding="utf-8") as file:
            file.write(result)
            print("Ваш результат записан в указанном файле:", args.output)

    else:
        print("Ваш результат:", result)

# запуск скрипта через "$ python3 app.py"
if __name__ == "__main__":
    main()
