import csv

# --- Lecture des données ---
def read_dataset(filepath):
    actions = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                name = row['name']
                price = float(row['price'])
                profit = float(row['profit'])
                if price > 0 and profit > 0:
                    actions.append((name, price, profit))
            except:
                continue
    return actions

# --- Algo optimisé façon "sac à dos 0/1" ---
def knapsack(actions, max_cost=500):
    n = len(actions)
    dp = [[0] * (int(max_cost * 100) + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        name, cost, profit = actions[i - 1]
        weight = int(cost * 100)
        value = cost * profit / 100
        for w in range(len(dp[0])):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    # --- Retrouver les actions choisies ---
    w = int(max_cost * 100)
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, cost, profit = actions[i - 1]
            selected.append(actions[i - 1])
            w -= int(cost * 100)
    return selected[::-1]

# --- Résultats ---
def print_results(title, actions):
    total_cost = sum(a[1] for a in actions)
    total_profit = sum(a[1] * a[2] / 100 for a in actions)
    print(f"\n=== {title} ===")
    for a in actions:
        print(f"{a[0]} - Coût: {a[1]}€, Bénéfice: {a[2]}%")
    print(f"Coût total: {total_cost:.2f}€")
    print(f"Bénéfice total: {total_profit:.2f}€")
    return total_cost, total_profit

# --- Données Sienna ---
sienna1 = [('Share-GRUT', 498.76, 39.42)]
sienna2 = [
    ('Share-ECAQ', 3166/100, 39.49), ('Share-IXCI', 2632/100, 39.4), ('Share-FWBE', 1830/100, 39.82),
    ('Share-ZOFA', 2532/100, 39.78), ('Share-PLLK', 1994/100, 39.91), ('Share-YFVZ', 2255/100, 39.1),
    ('Share-ANFX', 3854/100, 39.72), ('Share-PATS', 2770/100, 39.97), ('Share-NDKR', 3306/100, 39.91),
    ('Share-ALIY', 2908/100, 39.93), ('Share-JWGF', 4869/100, 39.93), ('Share-JGTW', 3529/100, 39.43),
    ('Share-FAPS', 3257/100, 39.54), ('Share-VCAX', 2742/100, 38.99), ('Share-LFXB', 1483/100, 39.79),
    ('Share-DWSK', 2949/100, 39.35), ('Share-XQII', 1342/100, 39.51), ('Share-ROOM', 1506/100, 39.23),
]

# --- Exécution ---
dataset1 = read_dataset("dataset1_Python+P7(2).csv")
dataset2 = read_dataset("dataset2_Python+P7.csv")

opt1 = knapsack(dataset1)
opt2 = knapsack(dataset2)

# Affichage comparé
print_results("Algo - Dataset 1", opt1)
print_results("Sienna - Dataset 1", sienna1)

print_results("Algo - Dataset 2", opt2)
print_results("Sienna - Dataset 2", sienna2)
