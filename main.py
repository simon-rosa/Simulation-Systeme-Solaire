from moteur import SystemeSolaire

def lancer_simulation():
    nom_choisi = input("Comment voulez-vous nommer votre système ? ")
    mon_systeme = SystemeSolaire(nom_choisi)
    print(mon_systeme.etoile)
    print("\nCONFIGURATION STELLAIRE...")
    print(mon_systeme.etoile)
    print("\nPlanètes découvertes :")
    for p in mon_systeme.planetes:
        print(p)

if __name__ == "__main__":
    lancer_simulation()