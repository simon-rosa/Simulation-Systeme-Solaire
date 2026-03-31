import math


class Etoile:

    puissances_spectrales: dict[str, float]= {
    "Naine Rouge":0.1,
    "Naine Jaune":1.0, 
    "Géante Bleue":100.0 
    }  

    def __init__(self, nom: str, type_spectral: str):
        self.nom = nom
        self.type_spectral = type_spectral
        self.luminosite = Etoile.puissances_spectrales.get(type_spectral, 1.0)

    def __str__(self):
        return f"{self.nom} | Type: {self.type_spectral} | Luminosité: {self.luminosite}"


class Planete:
    def __init__(self, nom: str, distance: float, masse: float, etoile_parente : Etoile):
        # distance est en UA (unité astronomiqe), 1 UA = 149 597 870,7 kilomètres soit la distance Terre-Soleil
        self.nom = nom
        self.distance = distance
        self.masse = masse
        self.etoile_parente = etoile_parente

    def estHabitable(self):
        L = self.etoile_parente.luminosite
        borne_inf = math.sqrt(L)*0.7
        borne_sup = math.sqrt(L)*1.5
        if borne_inf <= self.distance <= borne_sup:  
            return True
        else:
            return False
    
    def __str__(self):
        h = "OUI" if self.estHabitable() else "NON"
        return f"🪐 {self.nom} | Distance: {self.distance:.2f} UA | Habitable: {h}"