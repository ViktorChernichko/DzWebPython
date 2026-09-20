class Converter:
    conversion_count = 0

    @staticmethod
    def meters_to_feet(meters):
        Converter.conversion_count += 1
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        Converter.conversion_count += 1
        return feet / 3.28084

    @staticmethod
    def kilometers_to_miles(kilometers):
        Converter.conversion_count += 1
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        Converter.conversion_count += 1
        return miles / 0.621371

    @staticmethod
    def centimeters_to_inches(centimeters):
        Converter.conversion_count += 1
        return centimeters * 0.393701

    @staticmethod
    def inches_to_centimeters(inches):
        Converter.conversion_count += 1
        return inches / 0.393701

    @staticmethod
    def kilograms_to_pounds(kilograms):
        Converter.conversion_count += 1
        return kilograms * 2.20462

    @staticmethod
    def pounds_to_kilograms(pounds):
        Converter.conversion_count += 1
        return pounds / 2.20462

    @staticmethod
    def get_conversion_count():
        return Converter.conversion_count


if __name__ == "__main__":
    value_1 = Converter.meters_to_feet(10)
    value_2 = Converter.feet_to_meters(10)
    value_3 = Converter.kilometers_to_miles(5)
    value_4 = Converter.miles_to_kilometers(5)
    value_5 = Converter.centimeters_to_inches(50)
    value_6 = Converter.kilograms_to_pounds(70)

    print(f"10 m -> {value_1} ft")
    print(f"10 ft -> {value_2} m")
    print(f"5 km -> {value_3} mi")
    print(f"5 mi -> {value_4} km")
    print(f"50 cm -> {value_5} in")
    print(f"70 kg -> {value_6} lb")
    print(f"Total conversions: {Converter.get_conversion_count()}")
