import random
import sys

# Δημιουργία κενής λίστας για το ταμπλό
board = [" "] * 9
current_player = "X"
vs_cpu = True  # True = παίζεις εναντίον υπολογιστή, False = δύο παίκτες

# Όλες οι δυνατές νικητήριες γραμμές (οριζόντια, κάθετα, διαγώνια)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def reset():
    """Επαναφορά ταμπλό και παίκτη"""
    global board, current_player
    board = [" "] * 9
    current_player = "X"


def print_board(b):
    """Εμφάνιση ταμπλό"""
    print()
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print()


def ask_move(player):
    """Ζητά από τον παίκτη να επιλέξει θέση (1-9)"""
    while True:
        raw = input(f"Παίκτης {player}, θέση (1-9): ").strip()
        if not raw.isdigit():
            print(" Πληκτρολόγησε αριθμό 1-9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos > 8:
            print(" Εκτός ορίων. Δοκίμασε 1-9.")
            continue
        if board[pos] != " ":
            print(" Η θέση είναι κατειλημμένη.")
            continue
        return pos


def random_cpu_move():
    """Κίνηση του υπολογιστή"""
    free = [i for i, c in enumerate(board) if c == " "]
    return random.choice(free) if free else None


def check_win(b, player):
    """Έλεγχος αν ο παίκτης κέρδισε"""
    for a, c, d in WIN_LINES:
        if b[a] == b[c] == b[d] == player:
            return True
    return False


def is_draw(b):
    """Έλεγχος για ισοπαλία"""
    return all(cell != " " for cell in b)


def game_once():
    """Παίζει έναν ολόκληρο γύρο"""
    global current_player
    while True:
        print_board(board)
        if vs_cpu and current_player == "O":
            pos = random_cpu_move()
            print(f" Ο υπολογιστής παίζει στη θέση {pos + 1}")
        else:
            pos = ask_move(current_player)

        board[pos] = current_player

        if check_win(board, current_player):
            print_board(board)
            winner = "Υπολογιστής" if vs_cpu and current_player == "O" else f"Παίκτης {current_player}"
            print(f" {winner} κέρδισε!")
            return
        if is_draw(board):
            print_board(board)
            print(" Ισοπαλία!")
            return

        current_player = "O" if current_player == "X" else "X"


def main():

    print("Tic Tac Toe — Καλώς ήρθες! 🎮\n")
    mode = input("Θες 2 παίκτες (2), εναντίον υπολογιστή (1) ή να βγεις (0)? [1/2/0]: ").strip().lower()

    # Αν ο χρήστης επιλέξει να μην παίξει → τερματισμός
    if mode in ("0", "ο", "όχι", "οχι", "", "n", "no", "q", "quit", "exit"):
        print(" Τερματισμός. Καλή συνέχεια!")
        sys.exit(0)

    global vs_cpu
    vs_cpu = (mode != "2")
    while True:
        reset()
        game_once()
        again = input("Θες να ξαναπαίξεις; (ν/ο ή 0 για έξοδο): ").strip().lower()
        if again in ("0", "ο", "όχι", "οχι", "", "n", "no", "q", "quit", "exit") or (not again or again[0] != "ν"):
            print("Αντίο!")
            sys.exit(0)


if __name__ == "__main__":
    main()