def main():
    # Lecture des données d'entrée
    with open("Day19/input.txt", "r") as f:
        dss, towels = f.read().strip().split("\n\n")

    # Extraction des ensembles de chaînes
    ds = dss.split(", ")

    # Fonction pour compter les façons de construire une chaîne
    def count(s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Une seule façon de terminer une chaîne vide

        # Parcours inverse pour remplir dp
        for i in range(n - 1, -1, -1):
            dp[i] = sum(dp[i + len(t)] for t in ds if s.startswith(t, i))
        
        return dp[0]

    # Calcul du nombre total de façons de construire toutes les chaînes
    cnt = sum(count(towel) for towel in towels.split("\n"))
    print(cnt)


if __name__ == "__main__":
    main()
