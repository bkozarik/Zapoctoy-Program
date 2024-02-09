# Import knihovny Turtle pro grafické vykreslování
import turtle

def run():
  # Definice pravidel pro L-systém, který reprezentuje strom
  pravidla = {
      'M': ('S[+M][-M]SM'),  # Pravidlo pro hlavní větev stromu
      'S': ('SS')           # Pravidlo pro segment větve
  }
  rada = 'M'  # Počáteční řetězec pro generování stromu

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
    print('generace {}: {}'.format(q, lsystem(rada, pravidla, q)))

  # Inicializace grafického okna Turtle
  w = turtle.Screen()
  w.setup(width = 1.0, height = 1.0)  # Nastavení velikosti okna
  turtle.Turtle()

  # Generování řetězce pro vykreslení pomocí Turtle
  r = lsystem(rada, pravidla, opakovani)

  # Pozicování želvy na začátek kreslení
  turtle.penup()
  turtle.goto(0, -250)  # Umístění želvy na spodní část obrazovky
  turtle.pendown()
  turtle.left(90)  # Natočení želvy směrem nahoru

  # Seznamy pro ukládání pozic a úhlů želvy při kreslení větví
  pozice = []
  uhel = []

  # Procházení generovaného řetězce a vykreslování podle pravidel
  for pismenko in r:
      if pismenko == 'M':
          turtle.color('green')  # Barva pro hlavní větev
          turtle.forward(5)
          
      elif pismenko == 'S':
          turtle.color('brown')  # Barva pro segment větve
          turtle.forward(5)
          
      elif pismenko == '+':
          turtle.left(45)  # Otáčení želvy doleva
          
      elif pismenko == '-':
          turtle.right(45)  # Otáčení želvy doprava
          
      elif pismenko == '[':
          # Uložení aktuální pozice a úhlu při začátku větve
          a = turtle.pos()
          pozice.append(a)
          b = turtle.heading()
          uhel.append(b)
          
      elif pismenko == ']':
          # Návrat k poslední uložené pozici a úhlu při konci větve
          turtle.penup()
          turtle.goto(pozice.pop())  # Návrat na poslední pozici
          turtle.setheading(uhel.pop())  # Nastavení uloženého úhlu
          turtle.pendown()
