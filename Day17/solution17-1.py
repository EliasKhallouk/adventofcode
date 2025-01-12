import re

def main():
    # Lecture des données d'entrée
    with open("Day17/input.txt", "r") as f:
        content = f.read().strip().split("\n\n")
    regs, prog = content

    # Extraction des registres
    r = [
        int(re.match(r"Register [A-C]: (\d+)", s).group(1))
        for s in regs.splitlines()
    ]

    # Extraction du programme
    p = list(map(int, prog.split(": ")[1].split(",")))

    ip = 0

    # Fonction pour calculer une combinaison
    def combo():
        v = p[ip + 1]
        if 0 <= v <= 3:
            return v
        elif 4 <= v <= 6:
            return r[v - 4]
        else:
            raise ValueError(f"Invalid value v={v}")

    # Fonction pour effectuer une division par 2
    def div2(a, b):
        if b > 31:
            return 0
        return a >> b

    # Liste de sortie
    out = []

    # Exécution du programme
    while ip < len(p):
        if p[ip] == 0:
            r[0] = div2(r[0], combo())
        elif p[ip] == 1:
            r[1] ^= p[ip + 1]
        elif p[ip] == 2:
            r[1] = combo() & 7
        elif p[ip] == 3:
            if r[0] != 0:
                ip = p[ip + 1]
                continue
        elif p[ip] == 4:
            r[1] ^= r[2]
        elif p[ip] == 5:
            out.append(combo() & 7)
        elif p[ip] == 6:
            r[1] = div2(r[0], combo())
        elif p[ip] == 7:
            r[2] = div2(r[0], combo())
        else:
            raise ValueError(f"Invalid opcode {p[ip]}")
        ip += 2

    # Affichage du résultat
    print(",".join(map(str, out)))

if __name__ == "__main__":
    main()
