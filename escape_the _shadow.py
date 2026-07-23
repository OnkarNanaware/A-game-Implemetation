# game for the escape
# 33346 Onkar Nanaware assignment 1
import os
import heapq

# --- A* Pathfinding Logic ---

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def run_a_star(grid, start, goal):
    """
    Runs A* search and returns:
    - optimal_path: List of (r, c) tuples from start to goal
    - path_cost (G): Total steps along the optimal path
    - heuristic (H): Initial Manhattan distance from start to goal
    """
    start_node = Node(start)
    end_node = Node(goal)

    open_list = []
    heapq.heappush(open_list, (start_node.f, start_node))
    visited_g = {start: 0}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current.position == end_node.position:
            # Reconstruct complete path
            path = []
            curr = current
            while curr:
                path.append(curr.position)
                curr = curr.parent
            optimal_path = path[::-1]
            
            path_cost_g = current.g
            heuristic_h = manhattan_distance(start, goal)
            
            return optimal_path, path_cost_g, heuristic_h

        for dr, dc in directions:
            neighbor_pos = (current.position[0] + dr, current.position[1] + dc)
            r, c = neighbor_pos

            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#':
                tentative_g = current.g + 1

                if neighbor_pos not in visited_g or tentative_g < visited_g[neighbor_pos]:
                    visited_g[neighbor_pos] = tentative_g
                    neighbor_node = Node(neighbor_pos, current)
                    neighbor_node.g = tentative_g
                    neighbor_node.h = manhattan_distance(neighbor_pos, end_node.position)
                    neighbor_node.f = neighbor_node.g + neighbor_node.h
                    heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

    # Fallback if path is blocked
    return [start], 0, manhattan_distance(start, goal)

# --- Game Engine ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

MAZE = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "G", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "E", "#"]
]

def render_grid(grid, player_pos, ghost_pos, exit_pos, optimal_path, g_cost, h_cost):
    clear_screen()
    print("=== SHADOW ESCAPE (A* Pathfinding Assignment) ===")
    print("Roll No: 33346 | Name: Onkar Nanaware\n")
    print("Controls: W (Up), S (Down), A (Left), D (Right) | Q (Quit)\n")
    
    # Visual grid rendering
    for r in range(len(grid)):
        row_str = ""
        for c in range(len(grid[0])):
            pos = (r, c)
            if pos == player_pos:
                row_str += "P "
            elif pos == ghost_pos:
                row_str += "G "
            elif pos == exit_pos:
                row_str += "E "
            elif pos in optimal_path and pos != ghost_pos and pos != player_pos:
                row_str += "* "  # Visualize calculated optimal path tiles
            else:
                row_str += grid[r][c] + " "
        print(row_str)

    # --- Metrics required by assignment ---
    print("\n" + "="*50)
    print("📊 A* PATHFINDING METRICS (Ghost -> Player)")
    print("="*50)
    print(f"• Initial Heuristic (H - Manhattan Distance) : {h_cost}")
    print(f"• Total Optimal Distance / Path Cost (G)  : {g_cost} steps")
    print(f"• Combined Evaluation Cost (F = G + H)      : {g_cost + h_cost}")
    print(f"• Computed Optimal Path                     : {optimal_path}")
    print("="*50)

def main():
    player_pos = (1, 1)
    ghost_pos = (7, 11)
    exit_pos = (8, 11)

    move_map = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1)
    }

    while True:
        # Calculate A* path, total path cost (G), and heuristic (H)
        optimal_path, g_cost, h_cost = run_a_star(MAZE, ghost_pos, player_pos)
        
        # Render maze along with real-time A* metrics
        render_grid(MAZE, player_pos, ghost_pos, exit_pos, optimal_path, g_cost, h_cost)

        if player_pos == exit_pos:
            print("\n🎉 YOU ESCAPED! You reached the exit safely!")
            break
        if player_pos == ghost_pos:
            print("\n💀 GAME OVER! The Ghost caught you!")
            break

        move = input("\nYour move: ").strip().lower()
        if move == 'q':
            print("Exiting game...")
            break

        if move in move_map:
            dr, dc = move_map[move]
            new_r, new_c = player_pos[0] + dr, player_pos[1] + dc

            # Validate player movement
            if 0 <= new_r < len(MAZE) and 0 <= new_c < len(MAZE[0]) and MAZE[new_r][new_c] != '#':
                player_pos = (new_r, new_c)

            # Move ghost 1 step along the calculated optimal path
            if len(optimal_path) > 1:
                ghost_pos = optimal_path[1]

if __name__ == "__main__":
    main()