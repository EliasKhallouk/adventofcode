def main():
    # Lecture des données d'entrée
    with open("Day17/input.txt", "r") as f:
        content = f.read().strip().split("\n\n")
    _, prog = content

    # Extraction du programme
    out = list(map(int, prog.split(": ")[1].split(",")))

    c1 = -1
    c2 = -1

    # Structure attendue du programme
    expect_out = [
        2, 4, 1, "c1", 7, 5, 4, 3, 0, 3, 1, "c2", 5, 5, 3, 0
    ]

    expect_out = [
        (out[i] if s == "c1" else (out[i] if s == "c2" else s))
        if isinstance(s, str) else s
        for i, s in enumerate(expect_out)
    ]

    c1 = out[3]
    c2 = out[11]

    

    # Programme attendu
    """
    0: r1 = r0 and 7
    2: r1 = r1 xor c1
    4: r2 = div2(r0, r1)
    6: r1 = r1 xor r2
    8: r0 = div2(r0, 3)
    10: r1 = r1 xor c2
    12: out r1 and 7
    14: if (r0 != 0) goto 0
    """

    n = len(out) * 3
    solutions = []

    # Fonction de recherche
    def scan(k, b, f):
        if k == len(out):
            #print(f"-- {b}")
            solutions.append(b)
            return

        i = 3 * k  # Indice du bit
        b3 = (b >> i) & 7
        f3 = (f >> i) & 7

        for j in range(8):
            if b3 != (f3 & j):
                continue

            bu = b | (j << i)
            fu = f | (7 << i)

            # r1 = bits3[i] xor c1
            # out r1 xor bits3[i + r1] xor c2
            r1 = j ^ c1
            expect = out[k] ^ r1 ^ c2

            if not (0 <= expect <= 7):
                continue

            eb3 = (bu >> (i + r1)) & 7
            ef3 = (fu >> (i + r1)) & 7

            if eb3 != (ef3 & expect):
                continue

            bb = bu | (expect << (i + r1))
            ff = fu | (7 << (i + r1))

            scan(k + 1, bb, ff)

    # Initialisation de la recherche
    scan(0, 0, ~((1 << n) - 1) & ((1 << n) - 1))

    # Affichage du résultat
    print(min(solutions))


if __name__ == "__main__":
    main()
