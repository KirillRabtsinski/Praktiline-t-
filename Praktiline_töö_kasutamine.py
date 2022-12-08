#10
from math import *
print("Ajatesendus")
a=float(input("sisesta aja minutites"))
t=int(a//60)
sec=int(a%60)
print(f"minutes {t}:sekundid {sec}")





#9
from math import *
print("Rulluisutajad")
m=24/60
t=m*29.9
t=round(t,2)
print(f"Vastus: {t}km")
print()

#8 
from math import *
print("Kütusekulu arvutamine")
l=float(input("Kasutaja sisestab tangitud kütse liitrid"))
km=float(input("Kasutaja sisestab läbitud kilomeetrid"))
p=l/km*100
print (str(f"Vastus: {p}l/km"))
print()

#7
from math import *
print("Võtsite 3 sõbraga suure pitsa hinnaga 12,90€Jätate teenindajale 10% jootraha ")
s=10*12.90/100
s=round(s)
d=(12.90+s)
p=d/3
p=round(p,1)
print (str(f"Iga sõber peab mmaksma: {p}$"))
print()

#6
from math import *
from random import *
a=randint(1,99)
b=randint(1,99)
c=randint(1,99)
print(f"Külg a={a}\nkülg b={b}\nkülg c={c}")
print(f"Kolmnurga Ümbermõõt = {a+b+c}")



#5
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print(" ^^ '""' ^^")




#4
from math import *
a1=int(input("Sisesta 1. arv => "))
a2=int(input("Sisesta 1. arv => "))
a3=int(input("Sisesta 1. arv => "))
a4=int(input("Sisesta 1. arv => "))
a5=int(input("Sisesta 1. arv => "))
b=(a1+a2+a3+a4+a5)/5
print(f"Keskmine on {b}")

#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print("Sinu kiirus oli " + str(kiirus) + " km/h")



   
#2
from math import *
print("Ristkülikukujulise maatüki diagonaal") 
n=float(input("Sisesta ristküliku 1. külje pikkus => ")) 
m=float(input("Sisesta ristküliku 2. külje pikkus => ")) 
d=sqrt(n**2+m**2)
print(f"Maatiku diagonaal on {round (d,2)} m**2")


#1
from math import *
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrub {d}")

