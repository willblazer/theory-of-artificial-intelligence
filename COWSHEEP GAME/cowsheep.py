# -----------------------------
# COWS AND SHEEP SWAP PUZZLE
# -----------------------------

# Initial state
start_stable = ['C', 'C', 'C', 'C', 'E', 'S', 'S', 'S', 'S']

# Goal state
goal_stable = ['S', 'S', 'S', 'S', 'E', 'C', 'C', 'C', 'C']


# -------------------------------------------------
# FUNCTION 1: GENERATE ALL VALID NEXT MOVES
# -------------------------------------------------
def successors(stable):
    """
    Given a board state, generate all legal next states.
    """

    # Find index of empty space
    empty_index = stable.index('E')

    # Possible positions that could move into the empty space
    # (1 step left, 2 steps left, 1 step right, 2 steps right)
    possible_positions = [
        empty_index - 1,
        empty_index - 2,
        empty_index + 1,
        empty_index + 2
    ]

    # Check each possible position
    for pos in possible_positions:

        # Make sure position is inside board
        if 0 <= pos < len(stable):

            piece = stable[pos]

            # -----------------------------
            # RULES:
            # C moves right only
            # S moves left only
            # Can move 1 step
            # Can jump over 1 opposite piece
            # -----------------------------

            # C moving right
            if piece == 'C' and pos < empty_index:

                # If moving 1 step
                if empty_index - pos == 1:
                    new_state = stable.copy()
                    new_state[empty_index], new_state[pos] = new_state[pos], new_state[empty_index]
                    yield new_state

                # If jumping over 1 sheep
                elif empty_index - pos == 2 and stable[pos + 1] == 'S':
                    new_state = stable.copy()
                    new_state[empty_index], new_state[pos] = new_state[pos], new_state[empty_index]
                    yield new_state

            # S moving left
            elif piece == 'S' and pos > empty_index:

                # If moving 1 step
                if pos - empty_index == 1:
                    new_state = stable.copy()
                    new_state[empty_index], new_state[pos] = new_state[pos], new_state[empty_index]
                    yield new_state

                # If jumping over 1 cow
                elif pos - empty_index == 2 and stable[pos - 1] == 'C':
                    new_state = stable.copy()
                    new_state[empty_index], new_state[pos] = new_state[pos], new_state[empty_index]
                    yield new_state


# -------------------------------------------------
# FUNCTION 2: DEPTH-FIRST SEARCH (RECURSIVE)
# -------------------------------------------------
def solution(stable, depth=0):
    """
    Try to reach goal state using Depth-First Search.
    depth parameter is used only for printing indentation.
    """

    print("  " * depth + f"Exploring: {stable}")

    # Base case: If current state is goal
    if stable == goal_stable:
        print("  " * depth + "Goal reached!")
        return [stable]

    # Try every possible next move
    for next_state in successors(stable):

        print("  " * depth + f"Trying move -> {next_state}")

        result = solution(next_state, depth + 1)

        # If a solution is found deeper
        if result is not None:
            return [stable] + result

    # If no move leads to solution
    print("  " * depth + "Dead end, backtracking...")
    return None


# -------------------------------------------------
# RUN THE SOLVER
# -------------------------------------------------
print("Starting puzzle...\n")

path = solution(start_stable)

print("\nFinal Solution Path:\n")

if path:
    for step in path:
        print(step)
else:
    print("No solution found."