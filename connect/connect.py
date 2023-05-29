from dataclasses import dataclass, field
from enum import Enum
from itertools import cycle

HEIGHT = 6
WIDTH = 7

CONNECTIONS = 4


class Symbol(str, Enum):
    CROSS = "X"
    NOUGHT = "O"


class InvalidMove(Exception):
    pass


@dataclass
class Connect:
    height: int = HEIGHT
    width: int = WIDTH
    connections: int = CONNECTIONS
    _board: dict[tuple[int, int], Symbol] = field(default_factory=dict)

    def drop(self, player: Symbol, col: int) -> None:
        if not 0 <= col < self.width:
            raise InvalidMove(f"Column {col} is out of range")
        for row in reversed(range(self.height)):
            cell = row, col
            if cell not in self._board:
                self._board[cell] = player
                return None
        raise InvalidMove(f"Column {col} is full")

    def won(self) -> bool:
        return any(self._check_win(cell) for cell in self._board)

    def _check_win(self, cell: tuple[int, int]) -> bool:
        symbol = self._board[cell]
        row, col = cell
        # check right up
        if all(
            self._board.get((row + i, col - i)) == symbol
            for i in range(self.connections)
        ):
            return True
        # check right
        if all(
            self._board.get((row, col + i)) == symbol for i in range(self.connections)
        ):
            return True
        # check right down
        if all(
            self._board.get((row + i, col + i)) == symbol
            for i in range(self.connections)
        ):
            return True
        # check down
        if all(
            self._board.get((row + i, col)) == symbol for i in range(self.connections)
        ):
            return True
        return False

    def filled(self) -> bool:
        return len(self._board) >= self.height * self.width

    def show(self) -> None:
        line = ["_"] + [str(i) for i in range(self.width)]
        print("|".join(line))
        for row in range(self.height):
            line = [str(row)] + [
                self._board.get((row, col)) or "_" for col in range(self.width)
            ]
            print("|".join(line))


if __name__ == "__main__":
    connect = Connect()
    for player in cycle(Symbol):
        while True:
            connect.show()
            print()
            try:
                col = int(input(f"Column for {player}: "))
                connect.drop(player, col)
                break
            except ValueError:
                print("Not a number")
            except InvalidMove as e:
                print(e)

        if connect.won():
            connect.show()
            print(f"Player {player} has won!")
            print()
            break
        elif connect.filled():
            connect.show()
            print("It's a draw!")
            print()
            break
