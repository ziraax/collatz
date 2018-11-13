import numpy as np
import matplotlib.pyplot as plt
from math import *

def v(n):
  if n % 2 ==0:
    return n // 2
  return 3*n+1

def vol(n):
  """"vol de n (liste)"""
  res = [n]
  while n > 1:
    n = v(n)
    res.append(n)
  return res

def temps_vol(n):
  """ temps de vol de n"""
  return len(vol(n))-1

def altitude(n):
  """ altitude de n """
  return max(vol(n))

def voir_vol(n):
    """ Graphe du vol de n"""
    plage_x = vol(n)
    plt.plot(plage_x, marker=".", markersize=5)
    plt.grid()
    plt.title("Vol de n = " + str(n))
    plt.show()


def valuemaxtempsdevol(n):
    """ Entier plus petit que n ayant le plus grand temps de vol"""
    vmax, champ  = 0, 1
    for i in range(2 ,n+1):
        if temps_vol(i) > vmax:
            vmax = temps_vol(i)
            champ = i
    return champ

### On remarque que si n est congru a 4 modulo 6 alors les antécedents de n par la fonction v sont m=2n et m=(n-1)/3
### sinon le seulm antécédent de n par la fonction v est m=2n.

def classe_vol(n):
    """ Liste triée des entiers de temps de vol n """
    res = [1]
    for i in range(n):
        t = []
        for v in res:
            if (v % 6 == 4) and (v > 4):
                t.append((v-1) // 3)
            t.append(2*v)
        res = list(t)
    res.sort()
    return res

def suite_TV(n):
    """Liste des TV(i+1)/TV(i)"""
    res, TV = [1], [1]
    for i in range(n + 1):
        t = []
        for v in res:
            if (v % 6 == 4) and (v > 4):
                t.append((v-1) // 3)
            t.append(2*v)
        res = list(t)
        TV.append(len(res))

    plage_x = [TV[i+1] / TV[i] for i in range(n)]
    return plage_x

## On va tendre vers c = environ 1.263..., on peut alors chercher Tv(n) qui est environ égale à k*c^n
## on trouve avec la fonction classe_vol que k est environ égale à 0.664 (en resolvant l'équation kc^n=TV(n) avec n=28 ==> k approx= 460/1.263^28) et alors TV(n) environ égale à 0.664*c^n.

def approxtv(n):
    c = 1.2636004154018214
    return (int(0.664*(c**n)))

print("Bienvenue dans le programme sur la suite de Syracuse ! :")
print("Ce programme est constitué de 8 fonctions : vol(n), temps_vol(n), altitude(n), voir_vol(n) et valuemaxtempsdevol(n), classe_vol(n), suite_TV(n), approxtv(n), all(n) qui donne tout à la fois")
print("tv(n)=kc^n reste une approximation du nombre d'entiers dont le temps de vol est  égal à n, pour être plus précis mais beaucup moins efficace il faudrait regarder la taille de la liste générée par classe_vol(n) ")
print("la fonction suite_tv nous permet de trouver c, et n'est pas utile à part pour trouver approxtv(n)")
print("Choississez votre fonction :")

fonction = int(input("votre fonction ?(1=vol(n).2=temps_vol(n).3=altitude(n).4=voir_vol(n).5=valuemaxtempsdevol(n).6=classe_vol(n).7=suite_TV(n).8=approxtv(n)), 9=all(n)"))
n = int(input("choisissez n (n appartient à N >1)"))

if n < 1:
    print("N doit etre plus grand que 1")
else:

    if fonction == 1:
       print("Le vol de", n, "est de :", vol(n))
    elif fonction == 2:
       print("Le temps de vol de", n, "est de", temps_vol(n))
    elif fonction == 3:
       print("L'altitude de ", n, "est de", altitude(n))
    elif fonction == 4:
       print("Le graphe du vol de", n, "est celui ci"), voir_vol(n)
    elif fonction == 5:
       print("L'entier plus petit que", n, "ayant le plus grand temps de vol est", valuemaxtempsdevol(n))
    elif fonction == 6:
        print("La liste triée des entiers de temps de vol", n, "est", classe_vol(n), "avec un nombre TV(n) égale à :", len(classe_vol(n)))
    elif fonction == 7:
        print("La liste des TV(i+1/Tv(i)}", suite_TV(n))
    elif fonction == 8:
        print("Le nombre d'entiers dont le temps de vol est égal à", n, "est approximativement égale à", approxtv(n))
    elif fonction == 9:
        print("Le vol de", n, "est de :", vol(n))
        print("Le temps de vol de", n, "est de", temps_vol(n))
        print("L'altitude de ", n, "est de", altitude(n))
        print("Le graphe du vol de", n, "est celui ci"), voir_vol(n)
        print("L'entier plus petit que", n, "ayant le plus grand temps de vol est", valuemaxtempsdevol(n))
        print("La liste triée des entiers de temps de vol", n, "est", classe_vol(n), "avec un nombre TV(n) égale à :", len(classe_vol(n)))
        print("Le nombre d'entiers dont le temps de vol est égal à", n, "est approximativement égale à", approxtv(n))
    else:
        print("rentrez une valeur autorisé")


