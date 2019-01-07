

###cheminement qui a conduit au programme

##d'après mes cours de complément de maths ,
## le chiffrement correspond à une addition dans Z/26Z
##on pense alors l'esquisse de programme qui suit :


#nombre=int(input("numéro dans l'alphabet"))
#deca=int(input("décalage ?"))
#chiffrage=(deca+nombre)%26
#print(chiffrage)

##dans ce but , on rentre l'alphabet minuscule et majuscule :

#alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#alphamaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

##cependant , ce n'est pas  concluant , nous décidons de crypter en utilisant le code ascii , on obtient le programme qui suit :




###Entrées


phrase=input(str("Donnez votre phrase à crypter: "))
phrase=format(phrase)
deca=int(input("Entrez un décalage du code de César? "))


S=""


###Chiffrage

##après que l'utilisateur ai rentré sa phrase et le décalage , on traite les charactères 1 à 1
for i in range(0,len(phrase)):
    ##on code chacun des charactère avec la fonction "ord()" de python qui donne le code ascii
    nombre=ord(phrase[i])
    
    ##on ajoute une exception pour 32 qui correspond à l'espace 
    if nombre==32:
        S=S+" "
            
    else :
        chiffrage=((nombre-32)+deca)%223+32
            
        chara=chr (chiffrage)

        S=S+str(chara)
    
    
   

print(S)

R=""




###déchiffrage

for i in range(0,len(S)):
    nbre=ord(S[i])

    if nbre==32:
        R=R+" "
    else :
        chiffrag=((nbre-32)-deca)%223+32
        char= chr(chiffrag)
        R=R+str(char)


    

print(R)

