import readchar
from rich.console import Console
from rich.table import Table
from rich import box
from rich.live import Live

console = Console()
table = Table(show_header=True, header_style="bold", box=box.SQUARE)


pointer = 0

key = readchar.readkey()

with (Live(table) as live) :
        live.update(table)
        if key == readchar.key.UP:
            pointer = min(1, pointer - 1)
            if pointer == 1:
                table.add_column("[bold]MENU[/bold]")
                table.add_row("> Fight")
                table.add_row("See character stats")
                table.add_row("Inventory")
                console.print(table)
            elif pointer == 2:
                table.add_column("[bold]MENU[/bold]")
                table.add_row(" Fight")
                table.add_row(">See character stats")
                table.add_row("Inventory")
                console.print(table)
            elif pointer == 3:
                table.add_column("[bold]MENU[/bold]")
                table.add_row("Fight")
                table.add_row("See character stats")
                table.add_row("> Inventory")
                console.print(table)
            elif key == readchar.key.DOWN :
                pointer = max(3, pointer + 1)
                if pointer == 1 :
                    table.add_column("[bold]MENU[/bold]")
                    table.add_row("Fight")
                    table.add_row("> See character stats")
                    table.add_row("Inventory")
                    console.print(table)
                elif pointer == 2 :
                    table.add_column("[bold]MENU[/bold]")
                    table.add_row(" Fight")
                    table.add_row(">See character stats")
                    table.add_row("Inventory")
                    console.print(table)
                elif pointer == 3 :
                        table.add_column("[bold]MENU[/bold]")
                        table.add_row("Fight")
                        table.add_row("See character stats")
                        table.add_row("> Inventory")
                        console.print(table)


