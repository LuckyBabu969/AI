def cost(state):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def hill_climbing(state):
    print("Initial:")
    print(state)
    while True:
        current_cost = cost(state)

        if current_cost == 0:
            return state

        best_state = state
        best_cost = current_cost

        for col in range(4):
            for row in range(4):
                if state[col] != row:
                    neighbor = state.copy()
                    neighbor[col] = row
                    neighbor_cost = cost(neighbor)

                    if neighbor_cost < best_cost:
                        best_cost = neighbor_cost
                        best_state = neighbor
        print(best_state)
        print(best_cost)
        if best_state == state:
            return state

        state = best_state

initial_state = [0, 0, 0, 0]
result = hill_climbing(initial_state)

print("Final state:", result)
print("Final cost:", cost(result))