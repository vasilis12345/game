import readchar
from rich.console import Console
from rich.table import Table
from rich import box
from rich.live import Live
from virtualenv.discovery.cached_py_info import clear

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
                print(f"Health = {hero.health}\nAttack = {hero.attack}\nLevel = {hero.level}\nCrit_chance = {hero.critical_chance}\nXP requirement = {hero.xp_req}\nXP being held = {hero.xp_held}\nKill count = {hero.kill_count}")
                if key == readchar.key.RIGHT :
                    console.clear()
                    live.update(table)





























#                                      `::..   .
#                      `?XXX.  `T{/:.   %X/!!x "?x.
#                       "4{7@( '!+!!X(:.`4!!X!x.?h7h
#                     `!(:. ~!!!f(~!!!+!!{{.'~+h!tX!!?hh:.
#                '`X!.  !(d!X!!H!?{{``"!:?{{!{X*!?tX!!H*))h.
#              ...  '!X(!X!{{?@f!!!{!{x.!!%!!!%!!!)@Thh!!X)!).
#               ^!!!{:!(((!!: ~((({!!!h+!{{!X!+%?+{!!?!+)!+X(!+
#           -    `\tXX{(~!!!!!:.!.%%(!!!!!!!!!X!))!!!!X%``%!!!(>
#           ^X>:x. {!!!!X: ~!!*!{!!!{!~!X!)%!{!!!)?@!!!?!)?!!!>~
#             `X(!!:!!!{{(!!.)!%(:\!!:%~!~\!t!! `H!)~~!!!!!!(?@
#              `!X: `)!!!C44XX!!!.%%.X:>-> %!!X! /!~!.'!> !S!!!
#          +{..  \X%\.'{??X!!!t!!~!!{!~!~'.!~~~ -~` {> !~ /!X`
#            `X!XXM!!4!%\(4!!!!%(`,zccccd$$$$$$$$$ccx ` .~
#              "XLS@!)!!%L44X!!! d$$$$$$$$$$$$$$$$$$$,  '^
#               `!X?%:!!??X!4?*';$$$$$$$$$$$$$$$$$$$$$
#              `iXM:!!?Xt!XH!!! 9$$$$$$$$$$$$$$$$$$$$$
#              `X3tiXS#?WH!X!! $$$$$$$$$$$$$$$$$$$$$$
#              .MX?*StXX?X!!W? $$$$$$$>?$$$$$$$$$$$$
#                8??M%T%' r `  ;$$$$$$$$$,?$$$$$$$$$F
#                'StMX!': J$$d$$$$$$$$$$$$h ?$$$$$$"
#                 tM9MH d$$$$$$$$$$$$$$C???r{$$$F,r
#                 4M?t':$$$$$$$$$$$$$$$$h. $$$,cP"
#                 'M>.d$$$$$$$$$$$$$$$$$>d$$${.,
#                  ,d$$$$$$$$$$$$$$$$$'cd$$$$r"
#                  `$$$$$$$$$$$$$$$??$Jcii`?$h
#                   $$$$$$$$$$$$$F,;;, "?h,`$$h
#                 j$$$$$$$$$$$$$.CC>>>>c`"  `"        ..,g q,
#             .'!$$$$$$$$$$$$$' `''''''            aq`?g`$.Bk
#          ,- '  "?$$$$$$$$$$$$$$d$$$$$c, .         .)od$$$$$$
#      , -'           `""'   `"?$$$$$$$$$??=      .d$$$$$$$$F'
#    ,'                           `??$$P       .ed$$P""   `
#   ,                                `.      z$$$"
#  `:dbe,                          x,/    e$$F'
#   :$$$$P'`>                       $F  z$$$"
#  d$$$P"'  >                       $Fe$$$"
#.$$$?F     ;                       $$$$"
#$$$$$$eeu. >                       >P"
# `""???$$$$$eu,._''uWb,            )
#          `""??$P$$$$$$b.         :
#            >     ?$$$"'           {
#            F      `"              `:
#            >                       `>
#           >                        ?
#           J                          :
#           X                ..  .     ?
#           "{ 4{!~;/'!>{`~{>~.>! ~! '"
#            '>!>=.%=.;~~>~4~`{'>>>~!
#             4'!/>!\\!{~~:/{;!{;`;/=':
#             `=;!~:`~!>{.-; "(>=.':!;'
#              :;=.~{`;`~>!~> ?!/>>~!!{'
#              ~:~'!!;`;`~:>); ;(.uJL!~~
#                >L.(.:,L;L:-+d$$$$$$
#                :4$$$$$$$L   ?$$#$$$>
#                 '$$$B$$$>    $$$MB$&
#                 $$$$$$$      $$$@$F
#                  `$$$$$$>     R$$$$
#                   $$$$$$     {$$@$P
#                   $R$$$R     `!)=!>
#                   $$$6T       $$$$'
#                   $$R$B      ;$$$F,._
#                   !=!(!    .'        ``= .
#                   $$$$F    (.             '\
#                 ,{$$$$(      ``~'`` --:.._.,)
#                ;   ``  `-.
#                (          "\.
#                 ` -{._       ".
#                       `~:,._ .:
