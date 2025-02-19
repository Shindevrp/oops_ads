class BingoBoard:
    SIZE = 5

    def __init__(self, board):
        self.board = board
        self.marks = []
        
        for i in range(self.SIZE):
            row = []
            for j in range(self.SIZE):
                row.append(False)
            self.marks.append(row)

    def markNumbers(self, calledNumbers):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                for num in calledNumbers:
                    if self.board[i][j] == num:
                        self.marks[i][j] = True

    def isRowComplete(self, row):
        for j in range(self.SIZE):
            if not self.marks[row][j]:
                return False
        return True

    def isColumnComplete(self, column):
        for i in range(self.SIZE):
            if not self.marks[i][column]:
                return False
        return True

    def isMainDiagonalComplete(self):
        for i in range(self.SIZE):
            if not self.marks[i][i]:
                return False
        return True

    def isAntiDiagonalComplete(self):
        for i in range(self.SIZE):
            if not self.marks[i][self.SIZE - 1 - i]:
                return False
        return True

    def printBoard(self):
        for i in range(self.SIZE):
            row_display = ""
            for j in range(self.SIZE):
                if self.marks[i][j]:
                    row_display += "X  "
                else:
                    row_display += str(self.board[i][j]) + "  "
            print(row_display.strip())

class BingoGame:
    LETTERS = ["B", "I", "N", "G", "O"]

    def __init__(self, bingoBoard, calledNumbers):
        self.board = bingoBoard
        self.calledNumbers = calledNumbers
        self.bingoLetters = []

    def play(self):
        self.board.markNumbers(self.calledNumbers)
        
        for i in range(5):
            if self.board.isRowComplete(i):
                self.strikeLetter()
            if self.board.isColumnComplete(i):
                self.strikeLetter()
        
        if self.board.isMainDiagonalComplete():
            self.strikeLetter()
        if self.board.isAntiDiagonalComplete():
            self.strikeLetter()

        self.board.printBoard()
        self.printResult()

    def strikeLetter(self):
        if len(self.bingoLetters) < len(self.LETTERS):
            self.bingoLetters.append(self.LETTERS[len(self.bingoLetters)])

    def printResult(self):
        if len(self.bingoLetters) == len(self.LETTERS):
            result = ""
            for letter in self.bingoLetters:
                result += letter + " "
            print()
            print(result.strip())
            print("Game Completed!")
        else:
            remaining_letters = ""
            for i in range(len(self.bingoLetters), len(self.LETTERS)):
                remaining_letters += self.LETTERS[i] + " "
            print()
            print(f"Remaining Letters: {remaining_letters.strip()}")

def main():
    board = []
    for i in range(5):
        row = list(map(int, input().split()))
        board.append(row)
    
    calledNumbers = list(map(int, input().strip().split(',')))

    bingoBoard = BingoBoard(board)
    game = BingoGame(bingoBoard, calledNumbers)

    game.play()

if __name__ == "__main__":
    main()
