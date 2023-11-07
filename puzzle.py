"""
Program retuns bool statement after checking whether a column,
row or block has the same numbers.
link: https://github.com/hhafiya/kyrylova-iryna-lab8-task2.git
"""
def is_different(case: str) -> bool:
    """
    Function chechs whether it has the same numbers in string.
    Returns False or True
    >>> is_different(" 6  83  *")
    True
    >>> is_different("**3 3****")
    False
    """
    numbers = []
    for i in case:
        if i.isdigit():
            numbers.append(i)
    return len(numbers) == len(set(numbers))
def validate_board(board: list) -> bool:
    """
    Function checks whether it has the same numbers 
    in one line, column or block.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", \
"3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", \
"3   7  **", "  8  2***", "  2  ****"])
    True
    """
    for row in board:
        if not is_different(row):
            return False
    for column in range(9):
        col = ''.join([board[row][column] for row in range(9)])
        if not is_different(col):
            return False
    col_list = []
    row_list = []
    block_list_1 = []
    for column in range(9):
        col = ''.join([board[row][column] for row in range(9)])
        col_list.append(col)
    for row in board:
        row_list.append(row)
    k = 4
    for i in range(4, 9):
        block = row_list[i][k:k+5]
        block_list_1.append(block)
        k-=1
    p = 4
    block_list_2 =[]
    for i in range(0, 5):
        block_2 = col_list[i][p:p+4]
        block_list_2.append(block_2)
        p -= 1
    block_list_1 = list(reversed(block_list_1))
    block_list = [j + i for i, j in zip(block_list_1, block_list_2)]
    for block in block_list:
        if not is_different(block):
            return False
    return True
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())