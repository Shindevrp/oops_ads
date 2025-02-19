class Board:
    
    def __init__(self, size) -> None:
        self.size = size
        self.grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.grid.append(row)

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
        print("-" * (self.size * 4 - 1))

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        if self.grid[row][col] != " ":
            return False
        return True

    def place_move(self, row, col, symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        # Row 
        for i in range(self.size):
            win = True
            for j in range(self.size):
                if self.grid[i][j] != symbol:
                    win = False
                    break
            if win:
                return True

        # Col
        for j in range(self.size):
            win = True
            for i in range(self.size):
                if self.grid[i][j] != symbol:
                    win = False
                    break
            if win:
                return True

        #Diag
        win = True
        for i in range(self.size):
            if self.grid[i][i] != symbol:
                win = False
                break
        if win:
            return True

        # Anti-Diag
        win = True
        for i in range(self.size):
            if self.grid[i][self.size - i - 1] != symbol:
                win = False
                break
        if win:
            return True

        return False

    def isFull(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == " ":
                    return False
        return True

    def check_draw(self):  
        return self.isFull()

        
class Player:
    def __init__(self,symbol,name) -> None:
        self.symbol = symbol
        self.name = name

    def get_move(self):
        pass


class Game:
    def __init__(self,board,players,current_playes_index) -> None:
        self.board= board
        self.players =players
        self.current_player_index=current_playes_index

    def start(self):
        pass
    def switch_player(self):
        pass