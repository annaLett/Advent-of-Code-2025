"""
Advent of Code - Day 2 (Parte 2)
Obiettivo: trovare tutti gli ID formati da una sequenza ripetuta almeno due volte (es. 12341234 (1234 due volte), 123123123 (123 tre volte), 1212121212 (12 cinque volte), and 1111111 (1 sette volte))
e sommarli tutti.
"""

id_input = "67562556-67743658,62064792-62301480,4394592-4512674,3308-4582,69552998-69828126,9123-12332,1095-1358,23-48,294-400,3511416-3689352,1007333-1150296,2929221721-2929361280,309711-443410,2131524-2335082,81867-97148,9574291560-9574498524,648635477-648670391,1-18,5735-8423,58-72,538-812,698652479-698760276,727833-843820,15609927-15646018,1491-1766,53435-76187,196475-300384,852101-903928,73-97,1894-2622,58406664-58466933,6767640219-6767697605,523453-569572,7979723815-7979848548,149-216"

lista_range = id_input.split(",")


def id_non_validi(n: int) -> bool:
    s = str(n)
    L = len(s)

    # trova una qualsiasi sequenza base ripetuta >= 2 volte
    for seq_len in range(1, L):
        if L % seq_len != 0:
            continue

        ripetizioni = L // seq_len
        if ripetizioni < 2:
            continue

        base = s[:seq_len]
        if base * ripetizioni == s:
            return True

    return False


def somma_non_validi_da_range(lista_range: list[str]) -> int:
    """
    Prende una lista di range del tipo 'start-end',
    genera tutti i numeri nei range,
    controlla quali sono non validi,
    e restituisce la somma degli ID invalidi.
    """
    somma = 0

    for r in lista_range:
        start, end = r.split("-")
        start, end = int(start), int(end)

        for n in range(start, end + 1): # Itera tra tutti i numeri del range
            if id_non_validi(n):
                somma += n

    return somma


def main():
    print(f"Somma degli ID non validi: {somma_non_validi_da_range(lista_range)}")


if __name__ == "__main__":
    main()
