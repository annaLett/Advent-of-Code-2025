"""
Advent Of Code | DAY 3 | Code 2
"""

def max_number_from_row(riga: str, k: int) -> int:
    n = len(riga)
    result = []
    start = 0

    # scegliamo k cifre una alla volta (12.....1)
    for remaining in range(k, 0, -1):
        # devo lasciare spazio per le cifre restanti
        end = n - remaining + 1
        # prendo la cifra massima nel range individuato
        max_digit = max(riga[start:end])
        # prendo la posizione della cifra massima
        pos = riga.index(max_digit, start, end)

        result.append(max_digit)

        # aggiorno in punto di partenza
        start = pos + 1

    return int("".join(result))

totale = 0
with open("input.txt") as f:
    for idx, riga in enumerate(f, start=1):
        riga = riga.strip()
        if not riga:
            continue
        best = max_number_from_row(riga, 12)
        totale += best
        #print(f"Riga {idx}: max a 12 cifre = {best}")

print("Totale:", totale)
