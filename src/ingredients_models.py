import json


class Ingredient:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def from_dict(data):
        return Ingredient(name=data.get('name'))
    
# ingredients request object, including a list of ingredients
class IngredientsRequest:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @staticmethod
    def from_dict(data):
        ingredients = [Ingredient.from_dict(ingredient) for ingredient in data.get('ingredients')]
        return IngredientsRequest(ingredients=ingredients)
    
# recipe object, including a name, description, list of recipe ingredients, a list of recipe steps. each step includes a description and a order number. each ingredient includes a name and, quantity, and a unit of measure
class RecipeStep:
    def __init__(self, description, order):
        self.description = description
        self.order = order

    @staticmethod
    def from_dict(data):
        return RecipeStep(description=data.get('description'), order=data.get('order'))
    
class RecipeIngredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @staticmethod
    def from_dict(data):
        return RecipeIngredient(name=data.get('name'), quantity=data.get('quantity'), unit=data.get('unit'))

class Recipe:
    def __init__(self, name, description, ingredients, steps):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.steps = steps

    @staticmethod
    def from_dict(data):
        ingredients = [RecipeIngredient.from_dict(ingredient) for ingredient in data.get('ingredients')]
        steps = [RecipeStep.from_dict(step) for step in data.get('steps')]
        return Recipe(name=data.get('name'), description=data.get('description'), ingredients=ingredients, steps=steps)
    
    @staticmethod
    def example_json():
        example = {
            "name": "Chocolate Cake",
            "description": "A delicious and moist chocolate cake.",
            "ingredients": [
                {
                    "name": "Flour",
                    "quantity": 2,
                    "unit": "cups"
                },
                {
                    "name": "Sugar",
                    "quantity": 1.5,
                    "unit": "cups"
                },
                {
                    "name": "Cocoa Powder",
                    "quantity": 0.75,
                    "unit": "cup"
                },
                {
                    "name": "Baking Powder",
                    "quantity": 1.5,
                    "unit": "teaspoons"
                },
                {
                    "name": "Salt",
                    "quantity": 1,
                    "unit": "teaspoon"
                },
                {
                    "name": "Eggs",
                    "quantity": 2,
                    "unit": "units"
                },
                {
                    "name": "Milk",
                    "quantity": 1,
                    "unit": "cup"
                },
                {
                    "name": "Vegetable Oil",
                    "quantity": 0.5,
                    "unit": "cup"
                },
                {
                    "name": "Vanilla Extract",
                    "quantity": 2,
                    "unit": "teaspoons"
                },
                {
                    "name": "Boiling Water",
                    "quantity": 1,
                    "unit": "cup"
                }
            ],
            "steps": [
                {
                    "description": "Preheat your oven to 350°F (175°C). Grease and flour two nine-inch round pans.",
                    "order": 1
                },
                {
                    "description": "In a large bowl, stir together the sugar, flour, cocoa, baking powder, baking soda, and salt.",
                    "order": 2
                },
                {
                    "description": "Add the eggs, milk, oil, and vanilla, and mix for 2 minutes on medium speed of mixer.",
                    "order": 3
                },
                {
                    "description": "Stir in the boiling water last. Batter will be thin. Pour evenly into the prepared pans.",
                    "order": 4
                },
                {
                    "description": "Bake 30 to 35 minutes in the preheated oven, until the cake tests done with a toothpick.",
                    "order": 5
                },
                {
                    "description": "Cool in the pans for 10 minutes, then remove to a wire rack to cool completely.",
                    "order": 6
                }
            ]
        }
        return json.dumps(example, indent=4)
    
class RecipeResponse:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def from_dict(data):
        recipes = [Recipe.from_dict(recipe) for recipe in data.get('recipes')]
        return RecipeResponse(recipes=recipes)

