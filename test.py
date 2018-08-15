"""Task for Simbirsoft."""
import re
import sys
import os

paths = dict()


def initial(input_list):  # Проверка наличия/отсутствия файлов
    """Initializing."""
    try:
        if not os.path.exists(input_list[1]):
            raise FileNotFoundError("Файла с текстом не существует")

        if not os.path.exists(input_list[2]):
            raise FileNotFoundError("Файла со словарем не существует")

        if os.path.exists(input_list[3]):
            raise FileNotFoundError("Файл с таким именем существует")

    except FileNotFoundError:
        print(sys.exc_info()[1])

    except FileExistsError:
        print(sys.exc_info()[1])
    else:
        paths['path_to_text'] = input_list[1]  # Файл с текстом
        paths['path_to_dict'] = input_list[2]  # Файл со словарем
        paths['path_to_res'] = input_list[3]  # Результирующий файл


def main():
    """Main suite."""
    try:
        with open(paths['path_to_res'], "w", encoding="utf-8") as g:

            g.write("<!doctype html><html lang='ru'><head><meta charset='UTF-8'>\
<title>Document</title></head><body>")

            with open(paths['path_to_dict'], "r", encoding="utf-8") as d:

                words = d.read().split("\n")  # Составление
                tuple(words)                  # кортежа из словаря

                with open(paths['path_to_text'], "r", encoding="utf-8") as f:

                    for line in f:  # Идем по строкам из текста..
                        for word in words:  # И солвам из словаря.
                            line = re.sub(r"\b" + word + r"\b", "<i><b>" +  # Выделяем найденные
                                          word + "</i></b>", line)

                        g.write(line)
                        g.write("<br>")
            g.write("</body></html>")

    except UnicodeDecodeError:
        print("Пожалуйста, сохраните все файлы с кодировкой UTF-8")


if __name__ == '__main__':
    initial(sys.argv)

    if paths:  # Если пути к файлам корректны
        main()
