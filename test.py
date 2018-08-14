"""Fckn docstring."""
import re
import sys
import os

path_to_res = "res.html"
path_to_dict = "mes.txt"
path_to_text = "test.txt"


def main():
    """Return the pathname of the KOS root directory."""
    try:
        if os.path.exists(path_to_res):
            raise FileExistsError("Файл с таким именем существует.\
                                    Перезаписать?")
        else:
            with open(path_to_res, "w", encoding="utf-8") as g:
                g.write("<!doctype html><html lang='ru'><head><meta charset='UTF-8'>\
                         <title>Document</title></head><body>")

                if os.path.exists(path_to_dict):
                    with open(path_to_dict, "r", encoding="utf-8") as d:
                        words = d.read().split("\n")
                        tuple(words)
                else:
                    raise FileNotFoundError("Файла со словарем \
                                             не существует.")

                if os.path.exists(path_to_text):
                    with open(path_to_text, "r", encoding="utf-8") as f:

                        #  with open("mes.txt", "r", encoding="utf-8") as f:

                        for line in f:
                            for word in words:
                                # line = line.replace(word, "<i><b>" + word + "</i></b>")
                                line = re.sub(r"\b" + word + r"\b", "<i><b>" +
                                              word + "</i></b>", line)

                            g.write(line)
                            g.write("<br>")
                    g.write("</body></html>")
                else:
                    raise FileNotFoundError("Файла с текстом \
                                            не существует.")

    except UnicodeDecodeError:
        print("Пожалуйста, сохраните все файлы\
                 с кодировкой UTF-8")

    except FileNotFoundError:
        print(sys.exc_info()[1])

    except FileExistsError:
        print(sys.exc_info()[1])


if __name__ == '__main__':
    main()
