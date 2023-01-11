"""Programm zur Berechnung der Korrekturfunktion f1-f8 für Deformationsmethode 2.Ordnung"""

import numpy as np


def korrekturfunktion(L, S, E, I):

    # Deklaration
    f = np.empty(9)

    # Beiwert omega
    omega = L * np.sqrt(S / (E * I))

    # Korrekturfunktionen f1 bis f8
    f[1] = 1/12 * (omega**3 * np.sin(omega) / (2 - 2 * np.cos(omega) - omega * np.sin(omega)))

    f[2] = 1/6 * (omega**2 * (1 - np.cos(omega)) / (2 - 2 * np.cos(omega) - omega * np.sin(omega)))

    f[3] = 1/4 * (omega * (np.sin(omega) - omega * np.cos(omega)) / (2 - 2 * np.cos(omega) - omega * np.sin(omega)))

    f[4] = 1/2 * (omega * (omega - np.sin(omega)) / (2 - 2 * np.cos(omega) - omega * np.sin(omega)))

    f[6] = 1/3 * (4 * f[3]**2 - f[4]**2) / f[3]

    f[5] = f[6] - omega**2 / 3

    f[7] = (4 * f[3] * f[1] - 3 * f[2]**2) / f[1]

    f[8] = (-2 * f[4] * f[1] + 3 * f[2]**2) / f[1]

    print("Korrekturfunktionen:")
    for i in range(1, 9):
        print("f", i, "=", f[i])
    print("--------------------")


# Eingabewerte------------------------------
E = 2.1 * 10**8     # Elastizitätsmodul
I = 1 * 10**(-4)    # Flächenträgheitsmoment
A = 1 * 10**(-3)    # Stabquerschnitt

# Stab 12
S12 = 897.027   # Stab-Normalkraft
L12 = 9         # Stablänge

# Stab 13
S13 = 656.273
L13 = 9

# Stab 14
S14 = 800
L14 = np.sqrt(9**2 + 9**2)

korrekturfunktion(L12, S12, E, I)

korrekturfunktion(L13, S13, E, I)

korrekturfunktion(L14, S14, E, I)
