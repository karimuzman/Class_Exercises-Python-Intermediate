class Transaction:
    def __init__(self, debit, description, amount):
        self.debit = debit
        self.description = description
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __repr__(self):
        return f"Description: {self.description}, Amount: {self.amount}"


class Ledger:
    def __init__(self, account_type):
        self.account_type = account_type
        self.transactions = {}

    def add(self, transaction_id, transaction):
        self.transactions.update({transaction_id: transaction})

    def erase(self, transaction_id):
        del self.transactions[transaction_id]

    def __repr__(self):
        to_print = ""

        for key, value in self.transactions.items():
            to_print = to_print + \
                       "Id: " + str(key) + \
                       ", Item: " + value.description + \
                       ", Value: " + str(value.amount) + \
                       "\n"

        return to_print

    def __len__(self):
        i = 0
        for item in self.transactions:
            i += 1
        return i

    def __contains__(self, other):
        for value in self.transactions.values():
            if (value.description == other.description & value.amount == other.amount):
                return True
        return False

    def __getitem__(self, key):
        return self.transactions.get(key)

    def __setitem__(self, key, item):
        if not isinstance(item, Transaction):
            raise TypeError(f"Cannot set item of type {type(item)}")
        self.transactions[key] = item

    def __next__(self):
        if self.n < len(self.transactions):
            result = self.transactions.get(self.index[self.n])
            self.n += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        self.index = list(self.transactions.keys())
        self.n = 0
        return self


# Create a sales Ledger
sales_ledger = Ledger("Sales")

# Add transactions
transaction_1 = Transaction(True, "iPhone 12", 599)
sales_ledger.add(1, transaction_1)

transaction_2 = Transaction(True, "iPhone 13", 799)
sales_ledger.add(2, transaction_2)

transaction_56 = Transaction(True, "iPhone 14 Pro", 999)
sales_ledger.add(56, transaction_56)

transaction_108 = Transaction(True, "iPhe 14 Pro Mx", 199)
sales_ledger.add(108, transaction_108)

# 2. Print transaction
print(transaction_1)

# 3. Set correct transaction 108
transaction_108 = Transaction(True, "iPhone 14 Pro Max", 1099)
sales_ledger[108] = transaction_108

# 3. Get transaction and print
print(sales_ledger[108])

# 4. Iterate over all transactions and print description
for transaction in sales_ledger:
    print(transaction)
