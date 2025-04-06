class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients):
        self.recipes[name] = ingredients
        print(f'Recipe "{name}" added.')
        

    def view_recipe(self, name):
        if name not in self.recipes:
            print("Recipe not found!")
        else:
            print(self.recipes[name])

    def list_recipes(self):
        print(list(self.recipes.keys()))

n=int(input())

recipe_book = RecipeBook()

for _ in range(n):
    name = input().strip()
    ingredients = input().strip().split()
    recipe_book.add_recipe(name, ingredients)

recipe = input().strip()

recipe_book.view_recipe(recipe)
recipe_book.list_recipes()
