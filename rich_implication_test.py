from rich import print
from rich.layout import Layout

layout = Layout()

layout.split_column(
    Layout(name="Sprite area"),
    Layout(name="Text")
)
layout["Sprite area"].split_row(
    Layout(name="Hero box"),
    Layout(name="Enemy box"),
)


print(layout)