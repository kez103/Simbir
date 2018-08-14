import re

with open("res.html", "w", encoding="utf-8") as g:
    g.write('<!doctype html><html lang="ru"><head><meta charset="UTF-8"><title>Document</title></head><body>')

    with open("dict.txt", "r", encoding="utf-8") as d:
        words = d.read().split()
        tuple(words)

    # with open("test.txt", "r", encoding="utf-8") as f:
    with open("test.txt", "r") as f:
        for line in f:
            for word in words:
                # line = line.replace(word, "<i><b>" + word + "</i></b>")
                line = re.sub(r"\b" + word + r"\b", "<i><b>" + word + "</i></b>", line)

            g.write(line)
            g.write('<br>')
    g.write('</body></html>')