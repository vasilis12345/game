from rich.console import Console
from rich.live import Live
from rich.table import Table
import keyboard

console = Console()
table = Table()

pointer = 1





def choice() :
    if pointer == 1 :
        table.add_row(">Fight")
        table.add_row("See character stats")
        table.add_row("Inventory")
    elif pointer == 2 :
        table.add_row("Fight")
        table.add_row(">See character stats")
        table.add_row("Inventory")
    elif pointer == 3 :
        table.add_row("Fight")
        table.add_row("See character stats")
        table.add_row(">Inventory")

