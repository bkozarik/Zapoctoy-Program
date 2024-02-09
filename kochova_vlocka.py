# Import knihovny Turtle pro grafické vykreslování
import turtle

def run():
  # Počáteční řetězec pro L-systém, který definuje Kochovu vločku
  rada = ['F--F--F']

  # Pravidla pro transformaci řetězce v L-systému
  pravidla = {'F': 'F+F--F+F'}

  # Načtení počtu opakování (generací) od uživatele
  opakovani = int(input('počet generací: '))

  # Funkce pro generování řetězce L-systému na základě počátečního řetězce a pravidel
  def lsystem(rada, pravidla, opakovani):
    for _ in range(opakovani):
      x = []
      for pismenko in rada:
        if pismenko in pravidla:
          x += pravidla[pismenko]
        else:
          x += pismenko
      rada = x
    return rada

  # Výpis generovaných řetězců pro každou generaci
  for q in range(opakovani+1):
    print('generace {}: {}'.format(q, lsystem(rada,pravidla, q)))

  # Inicializace grafického okna Turtle
  w = turtle.Screen()
  #w.bgcolor('black')  # Nastavení barvy pozadí, aktuálně zakomentováno
  w.title('Kochova vločka')  # Titulek okna
  w.screensize()
  w.setup(width = 1.0, height = 1.0)  # Nastavení velikosti okna
  turtle.Turtle()
  #turtle.color('white')  # Nastavení barvy kreslení, aktuálně zakomentováno

  # Generování řetězce pro vykreslení pomocí Turtle
  r = lsystem(rada, pravidla, opakovani)

  # Nastavení rychlosti kreslení
  turtle.speed(1000)

  # Vykreslení Kochovy vločky na základě generovaného řetězce
  for pismenko in r:
    if pismenko == 'F':
      turtle.forward(5)  # Přesun vpřed
    elif pismenko == '-':
      turtle.right(60)  # Otáčení doprava o 60 stupňů
    elif pismenko == '+':
        turtle.left(60)  # Otáčení doleva o 60 stupňů
