from itertools import groupby


class TurkishLira:
    def __init__(self, date, transaction, coordinate, description):
        self.date = date
        self.transaction = transaction
        self.coordinate = coordinate
        self.description = description


class RecordingTransactions:
    def __init__(self):
        self.transactions_list = []

    def adding_transactions(self, date, transaction, coordinate, description):
        transaction_entry = TurkishLira(date, transaction, coordinate, description)
        self.transactions_list.append(transaction_entry)

    def print_out_days(self):
        self.transactions_list.sort(key=lambda p: p.date)
        for group in groupby(self.transactions_list, key=lambda p: p.date):
            for i in group[1]:
                print(group[0], i.transaction, i.coordinate, i.description)

