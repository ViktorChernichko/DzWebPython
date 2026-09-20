class Temperature:
    calculation_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius_degrees):
        Temperature.calculation_count += 1
        return celsius_degrees * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_degrees):
        Temperature.calculation_count += 1
        return (fahrenheit_degrees - 32) * 5 / 9

    @staticmethod
    def get_calculation_count():
        return Temperature.calculation_count


if __name__ == "__main__":
    value_1 = Temperature.celsius_to_fahrenheit(100)
    value_2 = Temperature.fahrenheit_to_celsius(32)
    value_3 = Temperature.celsius_to_fahrenheit(0)

    print(f"100 C -> {value_1} F")
    print(f"32 F -> {value_2} C")
    print(f"0 C -> {value_3} F")
    print(f"Total calculations: {Temperature.get_calculation_count()}")
