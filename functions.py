class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers
        for i in self.numbers:
            if not isinstance(i, int):
                raise ValueError("invalid input use a digit number only")

    def count(self):
        return len(self.numbers)

    def sum(self):
        total = 0
        for num in self.numbers:
            total += num
        return total

    @staticmethod
    def sum_of_two(x: int, y: int) -> int:
        return x+y