
class LuckyBingoBoard:
    size=4
    def __init__(self,size,board ) -> None:
        self.size=size
        # self.grid = grid
        self.board =board 
        self.marks = [[False] * LuckyBingoBoard.size for i in range(LuckyBingoBoard.size)]
    # def maek_number(self,num):
    #     for i in range(LuckyBingoBoard.size):
    #         for j in range(LuckyBingoBoard.size):
    #             if self.board[i][j] in num:
    #                 self.marks[i][j] = True


    def is_row_complette(self,row):
        return all(self.marks[row][col] for col in range(LuckyBingoBoard.size))
    def is_column_complete(self,col):
        return all(self.marks[row][col] for row in range(LuckyBingoBoard.size))
    def is_main_diagonal_complete(self):
        return all(self.marks[i][i] for i in range(LuckyBingoBoard.size))
    def is_anti_diagonal_complete(self):
        return all(self.marks[i][LuckyBingoBoard.size - 1 - i] for i in range(LuckyBingoBoard.size))
    def is_cross_complete(self):
        return all(self.marks[LuckyBingoBoard.size//2][i] for i in range(LuckyBingoBoard.size))
    def check_win(self):
        return self.check_bingo()

    def print_board(self):
        print("Board State:")
        for i in range(self.size):
            print(" ".join("X" if self.marks[i][j] else str(self.board[i][j]) for j in range(self.size)))
    
    


class Player:
    def __init__(self,name,board) -> None:
        self.name = name
        self.board = board
        self.marks=[[False] * LuckyBingoBoard.size for i in range(LuckyBingoBoard.size)]
        # self.grid = board
    #callednumber
    # def mark_number(self):
    def mark_number(self,num):
        for i in range(LuckyBingoBoard.size):
            for j in range(LuckyBingoBoard.size):
                if num == self.board[i][j]:  

                    self.marks[i][j] = True

    def has_won(self):
        # for i in range(self.board):
        #     if i.is_row_complette():
        #         return True
        #     if i.is_column_complete():
        #         return True
        # for i in range(self.board):
        #     if i.is_main_diagonal_complete():
        #         return True
        #     if i.is_anti_diagonal_complete():
        #         return True
        
        return (
        any(self.board.is_row_complette(i) for i in range(self.board.size)) or
        any(self.board.is_column_complete(i) for i in range(self.board.size)) or
        self.board.is_main_diagonal_complete() or
        self.board.is_anti_diagonal_complete()
    )

            

    def display_board(self):
        print(f"{self.name}'s Board:")
        self.board.print_board()


class LuckyBingoGame:
    def __init__(self,players,predefined_numbers) -> None:
        self.players = players
        self.predefined_numbers = predefined_numbers
        self.current_index = 0

    def play(self):
        turn_count = 1
        game_over = False

        while not game_over and self.predefined_numbers:
            current_player = 1 if turn_count % 2 == 1 else 2
            print(f"Player {current_player}'s turn!")

            called_number = self.predefined_numbers.pop(0)
            print(f"Number called: {called_number}")

            self.players.maek_number({called_number})
            self.players.print_card()

            if self.check_bingo():
                print(f"Player {current_player} wins!")
                game_over = True
            else:
                turn_count += 1

        if not game_over:
            print("The game is over, but no winner was found!")

def check_bingo(self):
        complete_lines = 0

        # Check for complete rows
        for row in range(LuckyBingoBoard.size):
            if self.LuckyBingoBoard.is_row_complete(row):
                complete_lines += 1

        # Check for complete columns
        for col in range(LuckyBingoBoard.size):
            if self.LuckyBingoBoard.is_column_complete(col):
                complete_lines += 1

        # Check for main diagonal
        if self.LuckyBingoBoard.is_main_diagonal_complete():
            complete_lines += 1

        # Check for anti diagonal
        if self.LuckyBingoBoard.is_anti_diagonal_complete():
            complete_lines += 1

        # If there are 5 complete lines (rows, columns, or diagonals)
        return complete_lines >= 4

