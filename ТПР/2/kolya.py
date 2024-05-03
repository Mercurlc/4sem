import numpy as np
import pandas as pd

crits = {
    "Калорийность": {"weight": 4, "direction": "max"},
    "Питательная ценность": {"weight": 3, "direction": "max"},
    "Время приготовления": {"weight": 5, "direction": "min"},
    "Доступность": {"weight": 5, "direction": "max"},
    "Цена": {"weight": 2, "direction": "min"}
}

alternatives = {
    "Овсянка с фруктами и орехами": [10, 10, 15, 15, 10],
    "Гречневая каша с овощами": [10, 10, 15, 10, 5],
    "Яичница с овощами": [5, 5, 5, 5, 5],
    "Смузи из зелени и фруктов": [5, 15, 5, 10, 10],
    "Творожная запеканка с ягодами": [15, 10, 10, 15, 5],
    "Тосты с авокадо и яйцом": [15, 10, 10, 10, 10],
    "Кускус с овощами и фетой": [5, 5, 10, 10, 5],
    "Йогурт с мюсли и свежими фруктами": [15, 15, 15, 15, 5],
    "Бутерброды с лососем": [10, 10, 5, 5, 5],
    "Бутерброд с сыром на козьем молоке": [10, 10, 15, 10, 10]
}

preference_matrix = pd.DataFrame(np.zeros((len(alternatives), len(alternatives))),
                                 index=alternatives.keys(), columns=alternatives.keys())

def calculate_P_N_D(alt1, alt2, crits):
    P, N = 0, 0
    for i, crit in enumerate(crits):
        weight = crits[crit]["weight"]
        direction = crits[crit]["direction"]
        a1, a2 = alt1[i], alt2[i]
        if a1 != a2:
            if (direction == "max" and a1 > a2) or (direction == "min" and a1 < a2):
                P += weight
            else:
                N += weight
    D = P / N if N != 0 else np.inf
    return P, N, D

for i, alt1 in enumerate(alternatives.keys(), start=1):
    for j, alt2 in enumerate(alternatives.keys(), start=1):
        if alt1 != alt2:
            P, N, D = calculate_P_N_D(np.array(alternatives[alt1]), np.array(alternatives[alt2]), crits)
            value_to_input = None
            if D>=1 and D != np.inf:
                value_to_input = np.round(D, 3)
            elif D == np.inf:
                value_to_input = np.inf
            else:
                value_to_input = -1
            preference_matrix.at[alt1, alt2] = value_to_input

print(preference_matrix.head())
preference_matrix = preference_matrix.applymap(lambda x: np.nan if isinstance(x, (int, float)) and x <= 2.4 else x)
print(preference_matrix.head())
