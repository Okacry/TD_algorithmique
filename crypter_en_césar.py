
#d'après mes cours de complément de maths ,
# le chiffrement correspond à une addition dans Z/26Z




nombre=int(input("numéro dans l'alphabet"))

deca=int(input("décalage ?"))

chiffrage=(deca+nombre)%26

print(chiffrage)
