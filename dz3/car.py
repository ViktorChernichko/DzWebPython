class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Введіть назву моделі: ")
        self.year = int(input("Введіть рік випуску: "))
        self.manufacturer = input("Введіть виробника: ")
        self.engine_volume = float(input("Введіть об'єм двигуна (л): "))
        self.color = input("Введіть колір машини: ")
        self.price = float(input("Введіть ціну: "))

    def print_data(self):
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} грн")

    def get_age(self, current_year):
        return current_year - self.year

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100
        return self.price

    def is_new(self, current_year, years_threshold=1):
        return self.get_age(current_year) <= years_threshold


if __name__ == "__main__":
    car = Car("Passat", 2015, "Volkswagen", 1.8, "Сірий", 450000)
    car.print_data()

    print(car.get_age(2026))
    print(car.apply_discount(10))
    print(car.is_new(2026))
