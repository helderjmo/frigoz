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