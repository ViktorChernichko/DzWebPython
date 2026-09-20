class Recipe:
    def __init__(self, title, author, recipe_type, description, video_link, ingredients, cuisine):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = list(ingredients)
        self.cuisine = cuisine

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_recipe_type(self):
        return self.recipe_type

    def set_recipe_type(self, recipe_type):
        self.recipe_type = recipe_type

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_video_link(self):
        return self.video_link

    def set_video_link(self, video_link):
        self.video_link = video_link

    def get_ingredients(self):
        return self.ingredients

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def get_cuisine(self):
        return self.cuisine

    def set_cuisine(self, cuisine):
        self.cuisine = cuisine


class RecipeView:
    @staticmethod
    def show(recipe):
        print("Recipe info:")
        print(f"Name: {recipe.get_title()}")
        print(f"Author: {recipe.get_author()}")
        print(f"Type: {recipe.get_recipe_type()}")
        print(f"Description: {recipe.get_description()}")
        print(f"Video link: {recipe.get_video_link()}")
        print(f"Cuisine: {recipe.get_cuisine()}")
        print("Ingredients:")
        for ingredient in recipe.get_ingredients():
            print(f"- {ingredient}")

    @staticmethod
    def show_error(message):
        print(f"Error: {message}")


class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_recipe(self):
        self.view.show(self.model)

    def add_ingredient(self, ingredient):
        if not ingredient:
            self.view.show_error("Ingredient name cannot be empty")
            return
        self.model.add_ingredient(ingredient)

    def remove_ingredient(self, ingredient):
        self.model.remove_ingredient(ingredient)

    def change_title(self, new_title):
        self.model.set_title(new_title)


if __name__ == "__main__":
    recipe_model = Recipe(
        title="Borscht",
        author="Olena Kovalchuk",
        recipe_type="first course",
        description="Traditional Ukrainian borscht with beet and cabbage",
        video_link="https://example.com/borscht",
        ingredients=["beet", "cabbage", "potato", "carrot", "onion"],
        cuisine="Ukrainian"
    )

    recipe_view = RecipeView()
    recipe_controller = RecipeController(recipe_model, recipe_view)

    recipe_controller.show_recipe()

    print()
    recipe_controller.add_ingredient("garlic")
    recipe_controller.remove_ingredient("carrot")
    recipe_controller.show_recipe()
