
from .expenser import *

def test_first():
    result = split(PARTICIPANTS, EXPENSES)

    assert _str(result) == """
Dima -> Alesya : 1300
Roman -> Alesya : 1800
Roman -> Oksana : 800
"""

def _str(expenses: list[Expense]):
    lines = [
        f"{expense.fr.name} -> {expense.to.name} : {expense.sum}"
        for expense in sorted(expenses)
    ]

    return "\n" + "\n".join(lines) + "\n"
