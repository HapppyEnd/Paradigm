"""Крестики-нолики."""


dashboard: list = [['-' for _ in range(3)] for _ in range(3)]

position: dict = {
    '1': [0, 0], '2': [0, 1], '3': [0, 2],
    '4': [1, 0], '5': [1, 1], '6': [1, 2],
    '7': [2, 0], '8': [2, 1], '9': [2, 2]
}


def print_dashboard(table: list) -> None:
    """Print dashboard."""
    for row in table:
        print(*row, sep='\t')
        print()


def move(table: list, number: int, sym: str) -> list:
    """Player move."""

    x, y = position.get(number)
    if table[x][y] != '-':
        raise ValueError('Cell is occupied')
    table[x][y] = sym
    return table


def check_win(board: list, element: str) -> bool:
    """Check winner."""
    win_list: list = [
        ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), ('1', '4', '7'),
        ('2', '5', '8'), ('3', '6', '9'), ('1', '5', '9'), ('3', '5', '7')]

    for i in win_list:
        x1, y1 = position.get(i[0])
        x2, y2 = position.get(i[1])
        x3, y3 = position.get(i[2])
        if (
                board[x1][y1] == element and
                board[x2][y2] == element and
                board[x3][y3] == element):
            return True
    return False


if __name__ == '__main__':
    symbol: str = 'X'
    count: int = 0
    check_list = [str(i) for i in range(1, 10)]
    while (data := input(f'{symbol} move: ')) not in ['q', 'exit', '']:
        print(f'{symbol} move')
        if data not in check_list:
            print('Incorrect input. Try again.')
            continue
        try:
            dashboard = move(dashboard, data, symbol)
        except ValueError:
            print('Cell is occupied')
            continue
        print_dashboard(dashboard)
        if check_win(dashboard, symbol):
            print(f'{symbol} win')
            break
        count += 1
        if count == 9:
            print('Nobody win.')
            break
        symbol = 'O' if symbol == 'X' else 'X'
