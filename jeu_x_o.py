import random
import os
import time
board=[]
for i in range(1, 10):
    board.append(str(i))
players = [{"name": "", "symbol": "X"}, {"name": "", "symbol": "O"}]
current_player_index = 0
game_mode = 0 

def display_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6: print("-" * 5)

def update_board(choice, symbol):
    if board[choice- 1].isdigit():
        board[choice- 1] = symbol
        return True
    return False

def reset_board():
    os.system('cls')
    global board
    board.clear()
    for i in range(1, 10):
        board.append(str(i))

def check_win_static(lst):
    win_combinations = [[0,1,2],[3,4,5],[6,7,8],
                        [0,3,6],[1,4,7],[2,5,8],
                        [0,4,8],[2,4,6]]
    for combination in win_combinations:
        if lst[combination[0]] == lst[combination[1]] == lst[combination[2]]:
            return lst[combination[0]]
    return None

def check_draw_static(lst):
    for cell in lst:
        if cell.isdigit():
           return False
    return True



def minimax(lst, depth, maximize):
    winner = check_win_static(lst)
    if winner == "O":
        return 10 - depth 
    if winner == "X": 
        return depth - 10  
    if check_draw_static(lst): return 0

    if maximize:
        best_score = -float('inf')
        for i in range(9):
            if lst[i].isdigit():
                temp = lst[i]
                lst[i] = "O"
                score = minimax(lst, depth + 1, False)
                lst[i] = temp
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if lst[i].isdigit():
                temp = lst[i]
                lst[i] = "X"
                score = minimax(lst, depth + 1, True)
                lst[i] = temp
                best_score = min(score, best_score)
        return best_score

def get_best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i].isdigit():
            temp = board[i]
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = temp
            if score > best_score:
                best_score = score
                move = i + 1
    return move
def display_machine_menu():
    while True:
        print("\n1. Facile\n2. Difficile\n0. Retour")
        try:
            choice = int(input("Choisissez la difficulté : "))
            if choice == 0:
                return None
            elif choice in [1, 2]:
                return choice
        except ValueError: print("Entrez un chiffre valide.")


def display_menu():
    while True:
        os.system('cls')
        print("1. Joueur vs Joueur\n2. Joueur vs Machine\n3. Règles\n0. Exit")
        try:
            mode = int(input("Choisissez le mode : "))
            if mode == 3:
                with open("regles.txt", "r") as f:
                    print(f.read())
                input("Cliquez sur Entrée pour retour...")
            elif mode == 0:
                exit()
            elif mode == 1:
                return 10  
            elif mode == 2:
                res = display_machine_menu()
                if res is not None:
                    return res 
        except ValueError:
            print("Entrez un chiffre valide.")
 
def setup_players():
    global game_mode
    game_mode = display_menu()
    players[0]["name"] = input("Nom du Joueur 1 : ")
    if game_mode == 10:
        players[1]["name"] = input("Nom du Joueur 2 : ")
    elif game_mode == 1:
        players[1]["name"] = "Machine_facile"
    elif game_mode == 2:
        players[1]["name"] = "Machine_difficile"
    

def play_game():
    global current_player_index
    while True:
        player = players[current_player_index]
        display_board()
        print(f"\nTour de {player['name']} ({player['symbol']})")

        while True:
            if current_player_index == 1 and game_mode in [1, 2]:
                time.sleep(1)
                if game_mode == 1:
                   available_moves = []
                   for cell in board:
                        if cell.isdigit():
                            available_moves.append(int(cell))
                   move = random.choice(available_moves)
                else :
                    move = get_best_move()
                print(f"La machine choisit la case {move}")
                update_board(move, player["symbol"])
                break
            else:
                try:
                    choice = int(input("Case (1-9) : "))
                    if 1 <= choice <= 9 and update_board(choice, player["symbol"]):
                        break
                    print("Case occupée ou invalide.")
                except ValueError: print("Entrez un chiffre.")

        if check_win_static(board):
            display_board()
            print(f"Félicitations ! {player['name']} a gagné !")
            return endgame_menu()
        elif check_draw_static(board):
            display_board()
            print("Égalité !")
            return endgame_menu()
        else:
            current_player_index = 1 - current_player_index

def endgame_menu():
    global current_player_index
    choix = input("\nTaper 1 pour Rejouer / other pour retour au Menu Principal ")
    reset_board()
    current_player_index = 0
    if choix == "1":
        return True
    else:
        return False
while True:
    setup_players()  
    while True:
        
        if play_game():
            continue  
        else:
            break     
