import csv
from datetime import datetime


# Lecture CSV
def read_actions_from_csv(file_path):
    actions = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                name = row['Action']
                cost = float(row['Coût'])
                profit_percent = float(row['Bénéfice'])
                if cost > 0 and profit_percent > 0:
                    profit = cost * profit_percent / 100
                    actions.append((name, int(cost), profit))  # coût en entier pour DP
            except ValueError:
                continue
    return actions

# Algo optimisé - type Knapsack 0/1
def optimized_best_investment(actions, max_budget):
    n = len(actions)
    budget = int(max_budget)

    # Initialisation de la matrice [n+1][budget+1]
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    start = datetime.now()
    # Remplissage de la matrice
    for i in range(1, n + 1):
        name, cost, profit = actions[i - 1]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + profit)
            else:
                dp[i][b] = dp[i - 1][b]

    # Récupération de la combinaison optimale
    b = budget
    selected_actions = []
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, cost, profit = actions[i - 1]
            selected_actions.append(actions[i - 1])
            b -= cost
    end = datetime.now()
    print(f"Temps d'exécution : {end - start}")
    return selected_actions, dp[n][budget]

# Point d’entrée
if __name__ == "__main__":
    actions = read_actions_from_csv("actions.csv")
    best_combo, best_profit = optimized_best_investment(actions, 500)

    print("Meilleure combinaison (optimisée) d'actions :")
    for action in best_combo:
        print(f"{action[0]} - Coût: {action[1]}€ - Bénéfice: {action[2]:.2f}€")

    print(f"\nCoût total : {sum(a[1] for a in best_combo)}€")
    print(f"Bénéfice total après 2 ans : {best_profit:.2f}€")
