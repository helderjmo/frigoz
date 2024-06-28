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


@app.route(route="recipe-image", methods=['POST'])
def recipie_image(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    recipe = req_body["recipe"]
    people = req_body["people"]

    client = OpenAI()

    response = client.images.generate(
    model="dall-e-3",
    prompt=f"A platter of {recipe}, for {people} people. If this dish is individual then give me an image of how it would come to the table. Make it good looking but realistic",
    n=1,
    size="1024x1024",
    )

    url = response.data[0].url

    return func.HttpResponse(url, status_code=200)