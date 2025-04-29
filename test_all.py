
from .expenser import *

def test_first():
    result = split(PARTICIPANTS, EXPENSES)

    assert _str(result) == """
Roman -> Oksana : 800
Dima -> Alesya : 1300
Roman -> Alesya : 1800
"""

{
    "R": 2600,
    "D": 2600,
    "O": 1300,
    "A": 3900,
}

def _str(expenses: list[Expense]):
    lines = [
        f"{expense.fr.name} -> {expense.to.name} : {expense.sum}"
        for expense in sorted(expenses)
    ]

    return "\n" + "\n".join(lines) + "\n"
