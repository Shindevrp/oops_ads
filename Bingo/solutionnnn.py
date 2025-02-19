class BingoCard:
    SIZE = 5

    def __init__(self, grid):
        self.grid = grid
        self.marks = [[False] * BingoCard.SIZE for _ in range(BingoCard.SIZE)]

    def mark_numbers(self, called_numbers):
        for i in range(BingoCard.SIZE):
            for j in range(BingoCard.SIZE):
                if self.grid[i][j] in called_numbers:
                    self.marks[i][j] = True

    def is_row_complete(self, row):
        return all(self.marks[row][col] for col in range(BingoCard.SIZE))

    def is_column_complete(self, col):
        return all(self.marks[row][col] for row in range(BingoCard.SIZE))

    def is_main_diagonal_complete(self):
        return all(self.marks[i][i] for i in range(BingoCard.SIZE))

    def is_anti_diagonal_complete(self):
        return all(self.marks[i][BingoCard.SIZE - 1 - i] for i in range(BingoCard.SIZE))

    def print_card(self):
        for i in range(BingoCard.SIZE):
            row_str = ""
            for j in range(BingoCard.SIZE):
                if self.marks[i][j]:
                    row_str += "X  "
                else:
                    row_str += f"{self.grid[i][j]}  "
            print(row_str.strip())


class BingoMatch:
    def __init__(self, bingo_card, called_numbers):
        self.bingo_card = bingo_card
        self.called_numbers = called_numbers
        self.number_queue = list(called_numbers)

    def play(self):
        turn_count = 1
        game_over = False

        while not game_over and self.number_queue:
            current_player = 1 if turn_count % 2 == 1 else 2
            print(f"Player {current_player}'s turn!")

            called_number = self.number_queue.pop(0)
            print(f"Number called: {called_number}")

            self.bingo_card.mark_numbers({called_number})
            self.bingo_card.print_card()

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
        for row in range(BingoCard.SIZE):
            if self.bingo_card.is_row_complete(row):
                complete_lines += 1

        # Check for complete columns
        for col in range(BingoCard.SIZE):
            if self.bingo_card.is_column_complete(col):
                complete_lines += 1

        # Check for main diagonal
        if self.bingo_card.is_main_diagonal_complete():
            complete_lines += 1

        # Check for anti diagonal
        if self.bingo_card.is_anti_diagonal_complete():
            complete_lines += 1

        # If there are 5 complete lines (rows, columns, or diagonals)
        return complete_lines >= 5


def main():
    # Input the bingo card grid
    bingo_card_grid = []
    for _ in range(5):
        row = list(map(int, input().split()))
        bingo_card_grid.append(row)

    # Input the called numbers
    called_numbers_str = input()
    called_numbers = set(map(int, called_numbers_str.split(',')))

    # Create the bingo card and game
    bingo_card = BingoCard(bingo_card_grid)
    bingo_game = BingoMatch(bingo_card, called_numbers)

    # Start the game
    bingo_game.play()


if __name__ == "__main__":
    main()