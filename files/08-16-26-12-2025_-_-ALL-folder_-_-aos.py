class Node:
    def __init__(self, name, heuristic, is_goal=False):
        self.name = name
        self.heuristic = heuristic
        self.is_goal = is_goal
        self.children = []
        self.marked = False

    def add_children(self, *child_nodes):
        for child_set in child_nodes:
            self.children.append(child_set)

def ao_star(node, path_cost):
    if node.is_goal:
        node.marked = True
        return node.heuristic

    if not node.children:
        return node.heuristic

    min_cost = float("inf")
    best_child_set = None

    for child_set in node.children:
        cost = 0
        for child in child_set:
            cost += child.heuristic + path_cost
            if not child.marked:
                cost += ao_star(child, path_cost)
        if cost < min_cost:
            min_cost = cost
            best_child_set = child_set

    if best_child_set:
        node.marked = True
        for child in best_child_set:
            child.marked = True

    return min_cost

# Create nodes
A = Node('A', 6)
B = Node('B', 4)
C = Node('C', 2)
D = Node('D', 0, is_goal=True)
E = Node('E', 0, is_goal=True)
F = Node('F', 0, is_goal=True)
G = Node('G', 0, is_goal=True)

# Build the graph
A.add_children([B, C])
B.add_children([D], [E])
C.add_children([F, G])

# Run AO* algorithm
print("Running AO* algorithm...")
total_cost = ao_star(A, path_cost=1)
print("Optimal solution path cost:", total_cost)

# Display solution path
def display_solution_path(node):
    if node.marked:
        print(node.name, end=" ")
        for child_set in node.children:
            for child in child_set:
                display_solution_path(child)

print("\nOptimal solution path:")
display_solution_path(A)
