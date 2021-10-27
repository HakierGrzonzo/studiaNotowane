#!/usr/bin/python3
from jinja2 import Template
from sys import argv

template = Template(open("./template.html").read())

data = []

def key(thing):
    return int(thing.strip("ou-.tx"))

for file in sorted(argv[1:], key=key):
    data.append((
        open(f"./inputs/{file}").read(),
        open(f"./outputs/out-{file}").read()
    ))

print(template.render(data=data))

