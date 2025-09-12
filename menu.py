import readchar
from rich.console import Console
from rich.table import Table
from rich import box
from rich.live import Live
from fighting import fight , hero

console = Console()
pointer = 1

with Live(Table(show_header=True, header_style="bold", box=box.SQUARE), refresh_per_second=10, console=console) as live:
    while True:
        table = Table(show_header=True, header_style="bold", box=box.SQUARE)
        table.add_column("[bold]MENU[/bold]")

        if pointer == 1:
            table.add_row("> Fight")
            table.add_row("See character stats")
            table.add_row("Inventory")
        elif pointer == 2:
            table.add_row("Fight")
            table.add_row("> See character stats")
            table.add_row("Inventory")
        elif pointer == 3:
            table.add_row("Fight")
            table.add_row("See character stats")
            table.add_row("> Inventory")

        live.update(table)

        key = readchar.readkey()

        if key == readchar.key.UP:
            pointer = max(1, pointer - 1)
        elif key == readchar.key.DOWN:
            pointer = min(3, pointer + 1)
        elif key == readchar.key.ENTER :
            if pointer == 1 :
                live.stop()
                fight()
            if pointer == 2 :
                live.stop()
                console.clear()
                print(f"Health = {hero.health}\nAttack = {hero.attack}\nLevel = {hero.level}\nCrit_chance = {hero.critical_chance}\nXP requirement = {hero.xp_req}\nXP being held = {hero.xp_held}")
                if key == readchar.key.RIGHT :
                    console.clear()
                    live.update(table)
