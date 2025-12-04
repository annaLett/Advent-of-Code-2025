"""
Advent Of Code | DAY 3 | Code 1
'Trova le due cifre più alte nella riga e scrivile nell’ordine in cui appaiono nella riga. 
"""

totale = 0

with open("input.txt", "r") as f:
    for riga in f:
        riga = riga.strip() # Rimuovo spazi bianchi per una corretta lettura
        if not riga:
            continue

        massimo = 0
        # ragioniamo per coppie quindi ho bisogno di un doppio indice
        # i prima cifra della coppia
        # j seconda cifra della coppia
        for i in range(len(riga) - 1):
            for j in range(i + 1, len(riga)):
                val = int(riga[i] + riga[j]) # creo la coppia
                if val > massimo:
                    massimo = val

        totale += massimo

print("Totale:", totale)