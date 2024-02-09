# Předpokládáme, že máte definované funkce run() pro každý fraktál ve vašich importovaných souborech
from gosperova_krivka import run as run_gosper
from hilbertova_krivka import run as run_hilbert
from kochova_antivlocka import run as run_koch_anti
from kochova_krivka import run as run_koch_curve
from kochova_vlocka import run as run_koch_snowflake
from strom import run as run_tree

def main():
    fractals = {
        "1": {"name": "Gosperova křivka", "function": run_gosper},
        "2": {"name": "Hilbertova křivka", "function": run_hilbert},
        "3": {"name": "Kochova antivločka", "function": run_koch_anti},
        "4": {"name": "Kochova křivka", "function": run_koch_curve},
        "5": {"name": "Kochova vločka", "function": run_koch_snowflake},
        "6": {"name": "Strom", "function": run_tree}
    }

    print("Vyberte fraktál k spuštění:")
    for key, value in fractals.items():
        print(f"{key}: {value['name']}")

    choice = input("Zadejte číslo fraktálu: ")

    if choice in fractals:
        print(f"Spouštění {fractals[choice]['name']}...")
        fractals[choice]['function']()
    else:
        print("Neplatný výběr.")

if __name__ == "__main__":
    main()
