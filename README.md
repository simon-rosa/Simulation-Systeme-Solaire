# 🌌 ExoPlanet-Generator

A lightweight Python simulation that procedurally generates random solar systems and calculates planetary habitability zones based on stellar astrophysics.

This project was developed to practice Python Object-Oriented Programming (OOP), type hinting, and procedural generation algorithms.

## ✨ Features
* **Procedural Generation:** Randomly generates a central star (Red Dwarf, Yellow Dwarf, or Blue Giant) and a system of 3 to 8 planets with varying masses and orbits.
* **Astrophysics Logic:** Calculates the habitability zone using the star's spectral luminosity (Distance D must fall between $0.7 \times \sqrt{L}$ and $1.5 \times \sqrt{L}$).
* **Object Composition:** Demonstrates clear relations between entities (a `Planet` object is linked to its parent `Star` object).

## 🛠️ Tech Stack
* **Language:** Python 3
* **Concepts:** OOP, Type Hinting, Procedural Generation, String Formatting (f-strings)
* **Libraries:** `math`, `random`

## 🚀 How to Run

Ensure you have Python 3 installed. Run the main simulation script:

```bash
python main.py
```

### 📊 Example Output
```text
Comment voulez-vous nommer votre système ? Kepler-186

CONFIGURATION STELLAIRE...
Etoile de Kepler-186 | Type: Naine Rouge | Luminosité: 0.1

Planètes découvertes :
🪐 Planète 1 | Distance: 1.05 UA | Habitable: NON
🪐 Planète 2 | Distance: 2.30 UA | Habitable: NON
🪐 Planète 3 | Distance: 3.12 UA | Habitable: NON
```
