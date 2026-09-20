class Fraction:
    object_count = 0

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        Fraction.object_count += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    @staticmethod
    def get_object_count():
        return Fraction.object_count


if __name__ == "__main__":
    first = Fraction(1, 2)
    second = Fraction(3, 4)
    third = first.add(second)

    print(f"First fraction: {first}")
    print(f"Second fraction: {second}")
    print(f"Sum: {third}")
    print(f"Total objects created: {Fraction.get_object_count()}")
