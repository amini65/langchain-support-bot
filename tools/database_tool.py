import json
from langchain.tools import tool

@tool
def get_product_price(peoduct_name: str) ->str:
    with open('data/products.json', 'r', encoding='utf-8') as f:
        data =json.load(f)


    for product in data['products']:
        if product_name.lower() in product['name'].lower():
            return f"Price of {product['name']}: {product['price']}"

    return f"Product '{product_name}' not found in database."



@tool
def list_all_products() -> str:
    """list of all products"""
    with open('data/products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    result = "Available Products:\n"
    for product in data['products']:
        result += f"- {product['name']}: {product['price']:,} \n"
    
    return result    