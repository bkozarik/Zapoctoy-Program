import turtle

def run():
    # Pravidla pro transformaci
    pravidla = {'L' : 'L+R++R-L--LL-R+',
                'R': '-L+RR++R+L--L-R'}
    rada = ['L']
    uhel = 60

    # Uživatelem definovaný počet opakování
    opakovani = int(input('Počet generací: '))

    # Funkce pro aplikaci L-systémových pravidel
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

    # Inicializace grafického rozhraní
    w = turtle.Screen()
    w.setup(width = 1.0, height = 1.0)
    turtle.Turtle() 
    k = lsystem(rada, pravidla, opakovani)
    turtle.speed(10000)

    # Nastavení počáteční pozice
    turtle.penup()
    turtle.goto(200,-200)
    turtle.pendown()
    turtle.colormode(255)

    # Inicializace barvy
    r,g,b = 255,0,0
    turtle.color(r,g,b)

    # Kreslení křivky podle vygenerované řady
    for pismenko in k:    
        if pismenko == 'L' or pismenko == 'R':
            turtle.forward(5)
            # Změna barvy podle pravidel
            if b >=0 and b < 255 and r == 255:
                b+=1                   
            elif r <= 255 and r >0 and g == 0 and b == 255:
                r -= 1               
            elif g < 230 and g >=0 and r == 0:
                g+=1               
            elif b > 0 and b <= 255 and r == 0:
                b-=1               
            elif r >=0 and r < 255 and g == 230:
                r+=1                       
            elif g >0 and g <= 230 and r == 255:
                g-=1            
        elif pismenko == '+':
            turtle.left(uhel)       
        elif pismenko == '-':
            turtle.right(uhel)  
        turtle.color(r,g,b)  
