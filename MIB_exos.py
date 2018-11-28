from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
Gardien = { Gardien.Nom for Gardien in BaseGardiens }
print("1. La réponse est ",Gardien)

### Question 2 : quel est l'ensemble des villes d'origine des agents?
Villes = { Agent.Ville for Agent in BaseAgents }
print("2.La réponse est ",Villes)

### Question 3 : quel est l'ensemble des triplets (no de cabine,alien,gardien) pour chaque cabine?
Triples = { (Alien.NoCabine, Alien.Nom, Gardien.Nom)
for Alien in BaseAliens
for Gardien in BaseGardiens if Gardien.NoCabine == Alien.NoCabine}
print("3. La réponse est ",Triples)

### Question 4 : quel est l'ensemble des couples (alien,allée) pour chaque alien:
Couples={(Alien.Nom, Alien.NoCabine) 
         for Alien in BaseAliens
        for Cabine in BaseCabine if Cabine.NoCabine == Alien.NoCabine}
print("4. La réponse est ",Couples)

### Question 5 : quel est l'ensemble de tous les aliens de l'allée 2 ?
Alien2={(Alien.Nom if Alien.NoCabine == Cabine.NoCabine and if Cabine.NoAllee == 2) 
        for Alien in BaseAliens}
print("5. La réponse est ",Alien2)

### Question 6 : quel est l'ensemble de toutes les planètes dont sont originaires les aliens habitant une cellule de numéro pair ?
Planetep={(Alien.Planete if Alien.NoCabine == 0 or Alien.NoCabine == 2 or Alien.NoCabine == 4 or Alien.NoCabine == 6 or Alien.NoCabine == 8) 
          for Alien in BaseALiens}
print("6. La réponse est ",Planetep)

### Question 7 : quel est l'ensemble des aliens dont les gardiens sont originaires de Terminus ?
AgT={(Alien.Nom if Gardien.Planete == 'Terminus') 
     for Alien in BaseAliens}
print("7. La réponse est ",AgT)

### Question 8 : quel est l'ensemble des gardiens des aliens féminins qui mangent du bortsch ?
gFb={(Guardien.Nom if Alien.Sexe == F and if Miam.Aliment == 'Bortsch') 
     for Guardien in BasesGuardiens}
print("8. La réponse est ",gFb)

### Question 9 : quel est l'ensemble des cabines dont les gardiens sont originaires de Terminus ou dont les aliens sont des filles ?
cToF={Cabine.NoCabine if Guardien.Planete == 'Terminus' or if Alien.Sexe == 'F') 
      for Alien in BaseAliens 
      for Guardien in BaseGuardiens}
print("9. La réponse est ",cToF)

### Question 10 : Y a-t-il des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange ?
print("10. La réponse est oui car Zorglub mange du Bortsch et est surveillé par Branno.")

### Question 11 : Y a-t-il des aliens originaires d'Euterpe ?
print("11. La réponse est oui car l'alien Blorx est originaire d'Euterpe.")

### Question 12 : Est-ce que tous les aliens ont un 'x' dans leur nom ?
print("12. La réponse est non car l'alien Zorglub n'a pas de 'x' dans son nom.")

### Question 13 : Est-ce que tous les aliens qui ont un 'x' dans leur nom ont un gardien qui vient de Terminus ?
print("13. La réponse est non car l'alien Urxiz a pour guardien Demerzel qui vient de la planète Uco.")

### Question 14 : Existe-t-il un alien masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Terminus ?
print("14. La réponse est oui car l'alien Zorglob est un alien masculin provenant de Trantor qui mange du bortsch.")
      
