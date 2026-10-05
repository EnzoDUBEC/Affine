def fonction(xA, xB, yA, yB):
 coef_directeur = (yA - yB) / (xA - xB)
 ordonne_origine = yA - coef_directeur *xA
 fonction = "y=" + str( coef_directeur ) + "* X +" + str(ordonne_origine)
 return fonction

xA =float (input ("l'abscisse de A ") )
yA =float (input ("l'ordonnée de A ") )
xB =float (input ("l'abscisse de B ") )
yB =float (input ("l'ordonnée de B ") )

print(fonction(xA, xB, yA, yB))
