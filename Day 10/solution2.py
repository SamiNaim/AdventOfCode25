import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

min_presses_sum = 0

def solve_machine(buttons, target):
    n_buttons = len(buttons)
    c = np.ones(n_buttons)
    
    A = np.array(buttons).T
    b = np.array(target, dtype=float)
    
    constraints = LinearConstraint(A, lb=b, ub=b)
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    return int(np.sum(result.x))

with open("input10.txt", "r") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        line.pop(0)
        joltages = list(map(int, line.pop().strip("{}").split(",")))
        buttons = []
        for b in line:
            button = list(map(int, b.strip("()").split(",")))
            button_list = [0] * len(joltages)
            for i in button:
                button_list[i] = 1
            buttons.append(button_list)

        min_presses = solve_machine(buttons, joltages)
        min_presses_sum += min_presses

print("The fewest button presses: ", min_presses_sum)