# Import modulu turtle pro kreslení grafiky
import turtle
def run():
  # Inicializace proměnných pro L-systém
  f = 'F'  # Základní symbol
  y = list('F+F--F+F')  # Pravidlo pro transformaci symbolu F
  rada = [f]  # Počáteční řada symbolů

  # Slovník pravidel pro transformaci symbolů
  pravidla = {f: y}

  # Získání počtu generací od uživatele
  opakovani = int(input('počet generací: '))

  # Definice funkce lsystem pro vytvoření řady symbolů na základě L-systému
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

  # Výpis generací a jejich řad
  for q in range(opakovani+1):
    print('generace {}: {}'.format(q, lsystem(rada, pravidla, q)))

  # Nastavení grafického prostředí pomocí modulu turtle
  w = turtle.Screen()
  w.bgcolor('black')  # Barva pozadí
  w.title('Kochova vločka')  # Titulek okna
  w.screensize()
  w.setup(width=1.0, height=1.0)  # Nastavení velikosti okna
  turtle.Turtle()
  turtle.color('white')  # Barva pera
  r = lsystem(rada, pravidla, opakovani)
  turtle.speed(1000)


  # Příprava želvy pro kreslení
  turtle.penup()
  turtle.goto(-400, -200)  # Počáteční pozice želvy
  turtle.pendown()

  # Kreslení Kochovy křivky na základě vygenerované řady symbolů
  for pismenko in r:
    if pismenko == 'F':
      turtle.forward(5)  # Pohyb dopředu
    elif pismenko == '-':
      turtle.right(60)  # Otočení doprava o 60 stupňů
    elif pismenko == '+':
        turtle.left(60)  # Otočení doleva o 60 stupňů
