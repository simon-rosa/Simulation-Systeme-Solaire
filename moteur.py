import random
from entites import Etoile, Planete


class SystemeSolaire:
    
    type_possible = [key for key in Etoile.puissances_spectrales.keys()]

    def __init__(self, nom_systeme: str):
        self.nom_systeme = nom_systeme

        type_choisi = random.choice(SystemeSolaire.type_possible)
        self.etoile = Etoile(f"Etoile de {nom_systeme}", type_choisi)

        self.planetes = []

        nombre_planete  = random.randint(3, 8)
        orbite_actuelle = 0.4
        
        for i in range(nombre_planete):
            orbite_actuelle += random.uniform(0.5,2.0)
            masse_aleatoire = random.uniform(0.1, 15.0)
            p = Planete(f"Planète {i+1}", orbite_actuelle, masse_aleatoire, self.etoile)
            self.planetes.append(p)