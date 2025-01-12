def main():
    # Lecture des données d'entrée
    with open("Day19/input.txt", "r") as f:
        dss, towels = f.read().strip().split("\n\n")

    # Extraction des ensembles de chaînes
    ds = dss.split(", ")

    # Fonction pour vérifier si une chaîne est possible
    def possible(s):
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True  # La fin de la chaîne est toujours valide

        # Parcours inverse pour remplir dp
        for i in range(n - 1, -1, -1):
            dp[i] = any(s.startswith(t, i) and dp[i + len(t)] for t in ds)
        
        return dp[0]

    # Compter les chaînes valides
    cnt = sum(1 for towel in towels.split("\n") if possible(towel))
    print(cnt)


if __name__ == "__main__":
    main()
