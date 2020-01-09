# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

print("Witaj w grze!")

def order():
    ask=input("Czy chcesz być pierwszy? t/n?")
    if ask.lower() == "t":
        print("Ok, jesteś pierwszy.")
        human = X
        computer = O
    if ask.lower() == "n":
        print("Ja zaczynam. Strzeż się!")
        computer = X
        human = O
    return computer, human

def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\t\t",board[0],"|",board[1],"|",board[2])
    print("\t\t","---------")
    print("\t\t",board[3],"|",board[4],"|",board[5])
    print("\t\t", "--------")
    print("\t\t", board[6], "|", board[7], "|", board[8],"\n")

def legal_moves(board):
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
           moves.append(square)
    return moves

def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """Odczytaj ruch człowieka."""
    legal = legal_moves(board)
    print("Dostępne są pola: ",legal)
    move = None
    while move not in legal:
        move = int(input("Jaki będzie Twój ruch?"))
        if move not in legal:
            print("\nTo pole jest już zajęte, niemądry Człowieku. Wybierz inne.\n")
    print("Znakomicie...")
    return move

def computer_move(board, computer, human):
    """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")
    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Zmień wykonawcę ruchu."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwycięzcy."""
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")
    if the_winner == computer:
        print("Jak przewidywałem, Człowieku, jeszcze raz zostałem triumfatorem. \n" \
    "Dowód na to, że komputery przewyższają ludzi pod każdym względem.")
    elif the_winner == human:
        print("No nie! To niemożliwe! Jakoś udało Ci się mnie zwieść, Człowieku. \n" \
    "Ale to się nigdy nie powtórzy! Ja, komputer, przyrzekam Ci to!")
    elif the_winner == TIE:
        print("Miałeś mnóstwo szczęścia, Człowieku, i jakoś udało Ci się ze mną " \
    "zremisować. \nŚwiętuj ten dzień... bo to najlepszy wynik, jaki możesz " \
    "kiedykolwiek osiągnąć.")

def main():

    computer, human = order()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")

