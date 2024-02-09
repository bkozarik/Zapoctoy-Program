import turtle
def run():
  # Počáteční řada a pravidla pro transformaci
  rada = ['F++F++F']
  pravidla = {'F': 'F+F--F+F'}

  # Uživatelem definovaný počet opakování
  opakovani = int(input('počet generací: '))

  # Funkce pro aplikaci L-systémových pravidel
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

  # Výpis generací pro kontrolu
  for q in range(opakovani+1):
    print('generace {}: {}'.format(q, lsystem(rada,pravidla, q)))

  # Inicializace grafického rozhraní
  w = turtle.Screen()
  w.title('Kochova vločka')
  w.setup(width = 1.0, height = 1.0)
  turtle.Turtle()

  # Generování a kreslení křivky podle vygenerované řady
  r = lsystem(rada, pravidla, opakovani)
  turtle.speed(1000)

  for pismenko in r:
    if pismenko == 'F':
      turtle.forward(5)  # Pohyb vpřed
    elif pismenko == '-':
      turtle.right(60)  # Otáčení doprava o 60 stupňů
    elif pismenko == '+':
        turtle.left(60)  # Otáčení doleva o 60 stupňů
