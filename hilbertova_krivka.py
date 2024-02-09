import turtle

def run():
    # Definice pravidel pro L-systém
    pravidla = {
        'x': ('+yF-xFx-Fy+'),
        'y': ('-xF+yFy+Fx-')
    }

    # Počáteční řetězec pro L-systém
    rada = ['x']

    # Načtení počtu opakování (generací) od uživatele
    opakovani = int(input('počet generací: '))

    # Funkce pro generování řetězce L-systému na základě počátečního řetězce a pravidel
    def lsystem(rada, pravidla, opakovani):
        for _ in range(opakovani):
            x = ''
            for pismenko in rada:
                if pismenko in pravidla:
                    x += pravidla[pismenko]
                else:
                    x += pismenko
            rada = x
        return rada

    # Výpis generovaných řetězců pro každou generaci
    for q in range(opakovani+1):
        print(f'generace {q}: {lsystem(rada, pravidla, q)}')

    # Inicializace grafického okna Turtle
    w = turtle.Screen()
    w.setup(width=1.0, height=1.0)  # Nastavení velikosti okna
    turtle.Turtle()

    # Příprava želvy pro kreslení
    turtle.penup()
    turtle.goto(-620, -280)  # Umístění želvy na začátek kreslení
    turtle.pendown()
    turtle.speed(10000)  # Nastavení rychlosti kreslení

    # Generování řetězce pro vykreslení
    r = lsystem(rada, pravidla, opakovani)

    # Vykreslení L-systému podle generovaného řetězce
    for pismenko in r:
        if pismenko == 'F':
            turtle.forward(10)  # Přesun vpřed
        elif pismenko == '+':
            turtle.left(90)  # Otáčení doleva o 90 stupňů
        elif pismenko == '-':
            turtle.right(90)  # Otáčení doprava o 90 stupňů
        # 'x' a 'y' jsou v tomto kontextu pouze pro generování vzoru a nevyžadují akci při kreslení

    turtle.done()  # Ukončení kreslení Turtle
