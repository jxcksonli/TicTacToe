""" 
The file contains details about: Tic Tac Toe Game
Date: 26/06/23
"""
import time

class TicTacToe():
    """
    Implements the game of Tic Tac Toe and all the relevant methods 
    """
    def __init__(self):
        """
        Initialises the gameboard for Tic Tac Toe
        """
        self.game_board = [[' - ' for _ in range(3)] for _ in range(3)]
        self.winner = None

    def print_gameboard(self):
        """
        Prints the gameboard
        """
        print("------------")
        for row in self.game_board:
            for item in row:
                print(item, end=" ")
            print()
        print("------------")
        return 
    
    def enter_value(self, row: int, column: int, value: str):
        """
        Enter the users input into the gameboard
        """
        self.game_board[row-1][column-1] = f" {value} "
    
    def check_result(self) -> str:
        """
        Lists possible winning combinations through rows, columns and diagonals
        Iterates across winning combinations to determine if one is found
        """
        winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]]

        for comb in winning_combinations:
            symbols = [self.game_board[row][col][1] for row, col in comb]
            if symbols == ["X", "X", "X"]:
                self.winner = "Player 1"
                return "Player 1 wins!"
            elif symbols == ["O", "O", "O"]:
                self.winner = "Player 2"
                return "Player 2 wins!"

        return ""

    def check_tie(self) -> bool:
        """
        O(1), checks all cells to determine whether there is a tie; occurs after checking if someone won
        """
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j].strip() not in ["X", "O"]:
                    return False
        return True
        
    def check_slot(self, row: int, column: int) -> bool:
        """
        O(1), Returns a boolean value to determine whether a Player can add the value into this slot
        """
        return self.game_board[row-1][column-1].strip() not in ["X", "O"]
            
    def start_game(self):
        """
        Starts the game of Tic Tac Toe
        """
        res = input(f"Welcome to this game of Tic Tac Toe!'\nIf you want to read the rules, type 'R'\nIf you want to start the game, type 'S'\n")
        while res.lower() != 's':
            if res.lower() == 'r':
                print("\nIn Tic-tac-toe, players take turns placing their symbol (X or O) on a 3x3 grid.\nThe goal is to create a line of three matching symbols in a row, column, or diagonal.\nThe game ends when a player wins, the board is full, or the game is a draw.\nSymbols cannot be moved once placed, and each move must be made on an empty cell.\n")
                res = input("Are we ready to start now? Type 'S' and let's begin!\n")
            else:
                res = input("Invalid input, please type 'R' to read the rules, 'S' to start\n")
        print("\nNote that Player 1 is cross and Player 2 is naughts")
        print("\nHere is the gameboard!\n")
        self.print_gameboard()

        count = 0
        players = [[2, "O"], [1, "X"]]
        
        while True:
            count = (count+1) % 2
            print(f"\nIt is now Player {players[count][0]}'s turn")

            res = input("Enter the row and column you want to enter with a comma separated (e.g 3,3)") #Will not account invalid answers
            while not self.check_slot(int(res[0]), int(res[-1])):
                res = input("Enter a valid row and column you want to enter with a comma separated (e.g 3,3)")
            self.enter_value(int(res[0]), int(res[-1]), players[count][1])
            
            self.print_gameboard()
            
            time.sleep(2)

            #Checks if the game is completed, either if a player wins or draw
            res = self.check_result()
            if "wins" in res:
                print(res)
                break

            if self.check_tie():
                print("\nGame is a tie! Thanks for playing :)\n")
                break

class MultiPlayTicTacToe(TicTacToe):
    """
    Implements multi-play for Tic Tac Toe using inheritance
    """
    def __init__(self, n: int):
        super().__init__()
        self.number_of_games = n
        self.player_1_score = 0
        self.player_2_score = 0

    def reset_board(self):
        """
        Resets the board after each game
        """
        self.game_board = [[' - ' for _ in range(3)] for _ in range(3)]
    
    def start_game(self):
        """
        Starts game for multi-play
        Inherits the child method of start_game but adds relevant attributes to check who wins after n rounds passes
        """
        print("You have selected a multiplay version\n")
        for _ in range(self.number_of_games):
            super().start_game()
            if "1" in self.winner:
                self.player_1_score += 1
            elif "2" in self.winner:
                self.player_2_score += 1
            self.reset_board()

        if self.player_1_score > self.player_2_score:
            return print(f"Player 1 wins with a total score of {self.player_1_score}")
        elif self.player_1_score < self.player_2_score:
            return print(f"Player 2 wins with a total score of {self.player_2_score}")
        return print(f"Both players draw with a score of {self.player_1_score}") #Tie
    
if __name__ == '__main__':
    #play = TicTacToe()
    #play.start_game()

    multiplay = MultiPlayTicTacToe(3)
    multiplay.start_game()

