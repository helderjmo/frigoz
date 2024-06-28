import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Import the IngredientsRequest class at the top of your file
from ingredients_models import IngredientsRequest, Recipe, RecipeResponse

@app.route('ingredients', methods=['POST'])
def ingredients(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for ingredients.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    # Convert the request JSON into an IngredientsRequest object
    ingredients_request = IngredientsRequest.from_dict(req_body)

    # # Now you can use the ingredients_request object
    # ingredient_names = [ingredient.name for ingredient in ingredients_request.ingredients]
    # return func.HttpResponse(f"Received ingredients: {', '.join(ingredient_names)}.", status_code=200)

    strjsonresult=Recipe.example_json()
    data = json.loads(strjsonresult)
    recipe = Recipe.from_dict(data)
    
    response_recipe = RecipeResponse(recipe)

    # return Http Response as a JSON with the response recipe serialized data
    return func.HttpResponse(response_recipe.to_json(), status_code=200)


@app.route(route="recipe-image")
def recipie_image(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )