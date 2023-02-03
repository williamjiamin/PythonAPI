# Created by williamjiamin
# For more info, follow me at Twitter: @WilliamjiaminEn
# More free tutorial Youtube: @Williamjiamin @learn-it-free @learn-finance-free

from flask import Flask
from flask import request

app = Flask(__name__)

tutorial_shops = [
    {
        "name": "Coding language tutorials Shop",
        "items": [
            {
                "name": "Python",
                "price": "9.99"
            }

        ]

    }

]


@app.get("/tutorial_shops")
def get_shop():
    return {"All Shops Names": tutorial_shops}


@app.post("/tutorial_shops")
def create_shop():
    request_data = request.get_json()
    new_shop = {"name": request_data["name"], "items": []}
    tutorial_shops.append(new_shop)
    return new_shop, 201


@app.post("/tutorial_shops/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for shop in tutorial_shops:
        if shop["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            shop["items"].append(new_item)
            return new_item, 201
    return {"message": "Sorry, I can't find your shop name"}, 404
