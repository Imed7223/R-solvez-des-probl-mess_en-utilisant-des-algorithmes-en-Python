import csv
import itertools
from datetime import datetime

# Lecture des actions depuis un fichier CSV
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
                    actions.append((name, cost, profit_percent))
            except ValueError:
                continue
    return actions

# Calcul du coût et du bénéfice total
def calculate_total(subset):
    total_cost = sum(a[1] for a in subset)
    total_profit = sum(a[1] * a[2] / 100 for a in subset)
    return total_cost, total_profit

start = datetime.now()
# Algo de force brute pour trouver la meilleure combinaison
def bruteforce_best_investment(actions, max_budget):
    best_profit = 0
    best_combo = []

    for r in range(1, len(actions) + 1):
        for combo in itertools.combinations(actions, r):
            total_cost, total_profit = calculate_total(combo)
            if total_cost <= max_budget and total_profit > best_profit:
                best_profit = total_profit
                best_combo = combo

    return best_combo, best_profit

# Point d’entrée principal
if __name__ == "__main__":
    actions = read_actions_from_csv("actions.csv")
    best_combo, best_profit = bruteforce_best_investment(actions, 500)
    end = datetime.now()
    print(end - start)
    print("Meilleure combinaison d'actions :")
    for action in best_combo:
        print(f"{action[0]} - Coût: {action[1]}€ - Bénéfice: {action[2]}%")

    print(f"\nCoût total : {sum(a[1] for a in best_combo)}€")
    print(f"Bénéfice total après 2 ans : {best_profit:.2f}€")

