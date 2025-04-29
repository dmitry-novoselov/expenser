
from itertools import groupby

class Participant:
    def __init__(self, name: str, weight: int = 1):
        self.name = name
        self.weight = weight

class Expense:
    def __init__(self, description: str, sum: int, participant: Participant):
        self.description = description
        self.sum = sum
        self.participant = participant

class Transfer:
    def __init__(self, fr: Participant, to: Participant, sum: int):
        self.fr = fr
        self.to = to
        self.sum = sum

    def __lt__(self, other):
        return (self.fr.name < other.fr.name or
                self.to.name < other.to.name or
                self.sum < other.sum)

Alesya = Participant("Alesya", weight=3)
Dima = Participant("Dima", weight=2)
Oksana = Participant("Oksana")

PARTICIPANTS = [
    Alesya,
    Dima,
    Oksana,
    Participant("Roman", weight=2),
]

EXPENSES = [
    Expense("meat", 7000, Alesya),
    Expense("greens", 1300, Dima),
    Expense("other", 2100, Oksana),
]

def split(participants: list[Participant], expenses: list[Expense]) -> list[Transfer]:
    total_sum = sum([e.sum for e in expenses])
    participants_number = sum([p.weight for p in participants])
    part = round(total_sum / participants_number)

    transfers = []

    balance = {
        participant: sum([e.sum for e in participant_expenses])
        for participant, participant_expenses in groupby(expenses, lambda e: e.participant)
    }

    for participant in participants:
        participant_spent = balance.setdefault(participant, 0)
        participant_part = part * participant.weight
        to_pay_others = participant_part - participant_spent

        for addressee in participants:
            if to_pay_others <= 0:
                break

            addressee_spent = balance[addressee]
            addressee_part = part * addressee.weight
            to_be_paid = addressee_spent - addressee_part

            if to_be_paid > 0:
                to_transfer = min(to_pay_others, to_be_paid)

                transfers.append(Transfer(participant, addressee, to_transfer))
                balance[participant] += to_transfer
                balance[addressee] -= to_transfer
                to_pay_others -= to_transfer

    return sorted(transfers)
