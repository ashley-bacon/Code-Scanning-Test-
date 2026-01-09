
import random
import sys
import time

GRID_SIZE = 5

def clear_screen():
    # Portable "clear" using prints; avoids OS-specific calls
    print("\n" * 50)

def banner():
    print("===================================")
    print("        TREASURE HUNT  v1.0        ")
    print("===================================")
    print("Find the treasure on a 5x5 grid!")
    print("Move with N/S/E/W. Beware of traps!\n")

def choose_difficulty():
    difficulties = {
        "1": ("Easy", 4, 4),   # (name, traps, lives)
        "2": ("Normal", 6, 3),
        "3": ("Hard", 8, 2)
    }
    while True:
        print("Choose difficulty:")
        print("[1] Easy   (4 traps, 4 lives)")
        print("[2] Normal (6 traps, 3 lives)")
        print("[3] Hard   (8 traps, 2 lives)")
        choice = input("> ").strip()
        if choice in difficulties:
            return difficulties[choice]
        print("Invalid choice. Try 1, 2, or 3.\n")

def random_position(exclude=None):
    while True:
        pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if not exclude or pos not in exclude:
            return pos

def compass_hint(player, treasure):
    px, py = player
    tx, ty = treasure
    dx = tx - px
    dy = ty - py
    hints = []
    if dy < 0:
        hints.append("North")
    elif dy > 0:
        hints.append("South")
    if dx > 0:
        hints.append("East")
    elif dx < 0:
        hints.append("West")
    if not hints:
        return "You're on it!"
    return " & ".join(hints)

def render_grid(player, visited, reveal=False, treasure=None, traps=None):
    # Render a minimal grid; player shown as 'P', visited as '.', unknown as '·'
    print("Grid:")
    for y in range(GRID_SIZE):
        row = []
        for x in range(GRID_SIZE):
            pos = (x, y)
            if pos == player:
                cell = "P"
