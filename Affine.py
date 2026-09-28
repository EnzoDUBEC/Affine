def fonction  ("xA, xB, yA, yB"):
 coef_directeur = (yA-yB) / (xA-xB)
 ordonne_origine = yA - coef_directeur *xA
 Xa =(input ("l'abscisse de A ") )
 Ya =(input ("l'ordonnée de A ") )
 Xb =(input ("l'abscisse de B ") )
 Yb =(input ("l'ordonnée de B ") )
 fonction = "y=" + str( coef_directeur ) + "* X +" + str(ordonne_origine)
 print(fonction(Xa, Xb, Ya, Yb))
