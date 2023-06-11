import json

def Ajoutvoiture():
     nbv = int(input("Saisir le nombre de voiture : "))  # le nombre de voiture  
    #========================Boucle========================
     for i in range(nbv):  
        matricule=int(input("saisir le matricule: "))
        marque=input("saisir la marque: ")
        nombre_portes=int(input("saisir le nombre des portes : "))
        print()
        
        voiture = { 'matricule' : matricule,
                 'marque': marque,
                 'nombre_portes' :nombre_portes}
        
        lesvoitures.append(voiture)
        

def Affichevoiture():
    i=1 # Compteur de voiture
    for v in lesvoitures: # pour chaque voiture On affiche  
        print()
        print('===============voiture '+ str(i)+ ' : =====')
        print('Les données de voitures : ')
        print('matricule :' ,v['matricule'])
        print('marque :' ,v['marque'])
        print('nombre_portes: ' ,v['nombre_portes'])
        i=i+1


def Sauvegardervoiture():
    f=open('lesvoitures.txt','w')    
    json.dump(lesvoitures,f);
    print("Fichier Sauvegarder avec Succee......")

def Restaurervoiture():
     global lesvoitures
     f=open('lesvoitures.txt','r')    
     lesvoitures =json.load(f);
     print("Fichier Restaurer avec Succee......")


def RechercheMat():
    c=int(input("Saisir le matricule: "))
    i=1
    for v in lesvoitures:
        if (c==v['matricule']):
            print()
            print("\n La Position de la voiture est: ",i)
            print("Matricule :   ",v['matricule'])
            print("Marque:  " ,v['marque'])
            print("Nombre:  " ,v['nombre_portes'])
            break
        i=i+1
    
def AfficheMenu():

        while(True):
         try:
            print("\t Menu")
            print("------------------------------------")    
            print("[1]- Ajout...")
            print("[2]- Affichage...")
            print("[3]- Sauvegarder...")
            print("[4]- Recherche par Matricule...")
            print("[5]- Exit...")
            choix=int(input("\t Donnez votre Choix: "))
            if(choix==1):
                print("Ajout voiture..... :")
                Ajoutvoiture()
            elif(choix==2):
                print("Affichage voiture.... :")
                Affichevoiture()
            elif(choix==3):
                print("Sauvegarder les voitures.... :")
                Sauvegardervoiture()
            elif(choix==4):
                print("Recherche Matricule.....")
                RechercheMat()
            elif(choix==5):
                break
            else:
                print("Choix de Menu invalide..!")    
         except:
            print("Erreur.....!")
            
voiture={}
lesvoitures=[]
Restaurervoiture()
AfficheMenu()
