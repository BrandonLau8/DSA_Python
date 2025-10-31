# Install PuLP if not installed:
# pip install pulp

from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

# Define the ILP problem
prob = LpProblem("ILP_Maximization", LpMaximize)

# Integer variables in [-15, 15]
x1 = LpVariable("x1", -15, 15, cat='Integer')
x2 = LpVariable("x2", -15, 15, cat='Integer')
x3 = LpVariable("x3", -15, 15, cat='Integer')
x4 = LpVariable("x4", -15, 15, cat='Integer')
x5 = LpVariable("x5", -15, 15, cat='Integer')

# Objective
prob += 2*x1 - 3*x2 + x3

# Constraints
prob += x1 - x2 + x3 <= 5
prob += x1 - x2 + 4*x3 <= 7
prob += x1 + 2*x2 - x3 + x4 <= 14
prob += x3 - x4 + x5 <= 7

# Solve
prob.solve(PULP_CBC_CMD(msg=0))

# Solution
solution = {v.name: v.value() for v in [x1, x2, x3, x4, x5]}
optimal_value = prob.objective.value()

print("Optimal solution:", solution)
print("Optimal objective value:", round(optimal_value, 2))

# Define LP problem
lp_prob = LpProblem("LP_Relaxation", LpMaximize)

# Continuous variables
x1 = LpVariable("x1", -15, 15, cat='Continuous')
x2 = LpVariable("x2", -15, 15, cat='Continuous')
x3 = LpVariable("x3", -15, 15, cat='Continuous')
x4 = LpVariable("x4", -15, 15, cat='Continuous')
x5 = LpVariable("x5", -15, 15, cat='Continuous')

# Objective
lp_prob += 2*x1 - 3*x2 + x3

# Constraints
lp_prob += x1 - x2 + x3 <= 5
lp_prob += x1 - x2 + 4*x3 <= 7
lp_prob += x1 + 2*x2 - x3 + x4 <= 14
lp_prob += x3 - x4 + x5 <= 7

# Solve
lp_prob.solve(PULP_CBC_CMD(msg=0))

# Solution
solution = {v.name: v.value() for v in [x1, x2, x3, x4, x5]}
optimal_value = lp_prob.objective.value()

print("LP relaxation solution:", solution)
print("LP relaxation optimal value:", round(optimal_value, 2))
