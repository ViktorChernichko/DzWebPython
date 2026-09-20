class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Введіть дату відкриття: ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

    def print_data(self):
        print(f"Назва: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def can_host(self, spectators_count):
        return spectators_count <= self.capacity

    def free_places(self, spectators_count):
        return self.capacity - spectators_count

    def is_large(self, threshold=40000):
        return self.capacity >= threshold


if __name__ == "__main__":
    stadium = Stadium("НСК Олімпійський", "1923-08-12", "Україна", "Київ", 70050)
    stadium.print_data()

    print(stadium.can_host(65000))
    print(stadium.free_places(65000))
    print(stadium.is_large())
