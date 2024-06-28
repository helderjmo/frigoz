import json
import azure.functions as func
import logging
from openai import OpenAI

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


    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"You are a kitchen assistant and when I give you my list of ingredients that I have available at the moment, you will give me a list of possible recipes with these ingredients so that I can make better use of these ingredients. The response to all requests should always be just a json with the following format: {Recipe.example_json()}"},
        {"role": "user", "content": ""}
    ]
    )

    strjsonresult=Recipe.example_json()
    data = json.loads(strjsonresult)
    recipe1 = Recipe.from_dict(data)
    recipe2 = Recipe.from_dict(data)
    
    
    #initialize the response recipe object with a list of recipes (use recipe1 and recipe2)
    response_recipe = RecipeResponse(recipes=[recipe1, recipe2])

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