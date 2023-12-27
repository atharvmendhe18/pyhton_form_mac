import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count
        self.mineai = MinesweeperAI(8, 8)

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # cannot use this approach
        # also i cannot access mines varible in minesweeperAI(why????)
        minesss = set({})
        for cell in self.cells:
            if cell in self.mineai.mines:
                minesss.add(cell)

        return minesss

        raise NotImplementedError

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        safess = set({})
        for cell in self.cells:
            if cell in self.mineai.safes:
                safess.add(cell)

        return safess

        raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        self.cells.remove(cell)
        self.count -= 1
        raise NotImplementedError

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        self.cells.remove(cell)
        raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set({(1, 2), (3, 4)})
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """

        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1st step
        self.moves_made.add(cell)

        # 2nd step
        self.safes.add(cell)

        # 3rd step
        # a) get all the neighbouring cells
        i, j = cell
        neighbouring_cells = set({})

        # a1) get cells in the sides

        if j != 0:
            neighbouring_cells.add((i, j - 1))
        if j != 7:
            neighbouring_cells.add((i, j + 1))

        # a2) get cells above and below
        if i != 0:
            neighbouring_cells.add((i - 1, j))
        if i != 7:
            neighbouring_cells.add((i + 1, j))

        # a3) get all four diagonal cells
            # get upper left diagonal
        if i != 0 and j != 0:
            neighbouring_cells.add((i - 1, j - 1))
            # get upper right diagonal
        if i != 0 and j != 7:
            neighbouring_cells.add((i - 1, j + 1))
            # get bottom left diagonal
        if i != 7 and j != 0:
            neighbouring_cells.add((i + 1, j - 1))
            # get bottom right diagonal
        if i != 7 and j != 7:
            neighbouring_cells.add((1 + 1, j + 1))

        # b) make a sentence and add to slef.knowledge
            # remove any known mines and safes from the sentence and update the count
        for mine in self.mines:
            if mine in neighbouring_cells:
                neighbouring_cells.remove(mine)
                count -= 1

        for safe in self.safes:
            if safe in neighbouring_cells:
                neighbouring_cells.remove(safe)

        self.knowledge.append(Sentence((neighbouring_cells), count))

        # 4th step
        # lets check the basic cases first when the count = 0 and count = len(cells)
        # do i need to do this? => YES
        for sentence in self.knowledge:
            set_cell = sentence.cells
            if sentence.count == 0 and len(set_cell) != 0:
                for cell in set_cell:
                    self.mark_safe(cell)

            if sentence.count == len(set_cell):
                for cell in set_cell:
                    self.mark_mine(cell)

        # is forth step complete??

        # 5th step
        snetence1 = self.knowledge[0]
        set1 = snetence1.cells
        for i in range(1, len(self.knowledge)):
            sentencei = self.knowledge[i]
            seti = sentencei.cells
            if seti.issubset(set1) or seti.issuperset(set1):
                new_set = set1.intersection(set1)
                new_count = sentencei.count - snetence1.count
                if new_count < 0:
                    new_count = -1 * new_count
                self.knowledge.append(Sentence(new_set, new_count))

        raise NotImplementedError

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        for i in range(8):
            for j in range(8):
                if (((i, j) not in self.moves_made) and ((i, j) not in self.mines) and ((i, j) in self.safes)):
                    return (i, j)
        return None
        raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        for i in range(8):
            for j in range(8):
                if (((i, j) not in self.mines) and ((i, j) not in self.moves_made)):
                    return (i, j)

        return None

        raise NotImplementedError


def main():
    board1 = Minesweeper(4, 4, 8)
    minesweeper1 = MinesweeperAI(4, 4)
    sentence1 = Sentence(set({(1, 2), (2, 1), (3, 2), (0, 0), (3, 4)}), 2)
    minesweeper1.add_knowledge((1, 1), 2)


main()
