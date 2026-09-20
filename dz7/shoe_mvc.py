class Shoe:
    def __init__(self, gender_type, kind, color, price, manufacturer, size):
        self.gender_type = gender_type
        self.kind = kind
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def get_gender_type(self):
        return self.gender_type

    def set_gender_type(self, gender_type):
        self.gender_type = gender_type

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size


class ShoeView:
    @staticmethod
    def show(shoe):
        print("Shoe info:")
        print(f"Type: {shoe.get_gender_type()}")
        print(f"Kind: {shoe.get_kind()}")
        print(f"Color: {shoe.get_color()}")
        print(f"Price: {shoe.get_price()}")
        print(f"Manufacturer: {shoe.get_manufacturer()}")
        print(f"Size: {shoe.get_size()}")

    @staticmethod
    def show_error(message):
        print(f"Error: {message}")


class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_shoe(self):
        self.view.show(self.model)

    def change_price(self, new_price):
        if new_price < 0:
            self.view.show_error("Price cannot be negative")
            return
        self.model.set_price(new_price)

    def change_size(self, new_size):
        self.model.set_size(new_size)

    def change_color(self, new_color):
        self.model.set_color(new_color)


if __name__ == "__main__":
    shoe_model = Shoe(
        gender_type="male",
        kind="sneakers",
        color="black",
        price=1500,
        manufacturer="Nike",
        size=42
    )

    shoe_view = ShoeView()
    shoe_controller = ShoeController(shoe_model, shoe_view)

    shoe_controller.show_shoe()

    print()
    shoe_controller.change_price(1350)
    shoe_controller.change_size(43)
    shoe_controller.show_shoe()
