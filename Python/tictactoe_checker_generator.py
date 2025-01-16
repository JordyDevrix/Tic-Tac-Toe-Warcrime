def generate_tic_tac_toe_winner_checker():
    board_positions = ['X', 'O', '-']  # X, O, and Empty space

    # The indices for the winning positions in a 3x3 grid
    winning_combinations = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6],  # Diagonal 2
    ]

    def check_win(board):
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != '-':
                return board[combination[0]]  # Return the winner ('X' or 'O')
        return None  # No winner

    # Generate all possible combinations (3^9 = 19683 possible board configurations)
    board_configurations = []
    for i in range(19683):
        board = []
        num = i
        for j in range(9):
            board.append(board_positions[num % 3])
            num //= 3
        board_configurations.append(board)

    # Write the checker function with 19683 if statements
    script = "def check_tic_tac_toe_winner(board):\n"
    for i, board in enumerate(board_configurations):
        board_str = ''.join(board)
        # We need to check if the board configuration has a winner
        winner = check_win(board)
        statement = "elif"

        if i == 0:
            statement = "if"

        if winner:
            script += f"    {statement} board == '{board_str}':\n        return '{winner}'\n"
        else:
            script += f"    {statement} board == '{board_str}':\n        return None\n"

    loop = """
game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

players = ['X', 'O']
turn = 0

while True:
    player = 'X' if turn % 2 == 0 else 'O'
    print(f'Player {player}')

    x_cor = int(input(' Enter X cor: '))
    y_cor = int(input(' Enter Y cor: '))

    if game[y_cor][x_cor] == '-':
        game[y_cor][x_cor] = player
    else:
        print('This position has already been chosen')
        continue

    check_game = ''
    for row in game[::-1]:
        cur_game = ''
        for col in row:
            cur_game += ' ' + col
            check_game += col
        print(cur_game)
        
    winner = check_tic_tac_toe_winner(check_game)
    if winner == 'X' or winner == 'Y':
        print(f'Winner is {winner}')
        exit(0)
    
    turn += 1
    
    """

    script += loop

    # Write the function to a Python file
    with open("tictactoe_winner_checker.py", "w") as f:
        f.write(script)


# Call the function to generate the script
generate_tic_tac_toe_winner_checker()
