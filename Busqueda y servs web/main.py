from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()
 
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
 
products = [
    {"id": 1, "name": "product 1", "price": 20, "stock": 10},
    {"id": 2, "name": "product 2", "price": 30, "stock": 11}
]
 
@app.get('/products')
def get_products():
    return products
 
@app.get('/')
def message():
    return "hola"
 
@app.get('/products/{id}')
def get_product(id: int):
    return next((item for item in products if item['id'] == id), None)
 
@app.get('/products/')
def get_products_by_stock(stock: int, price: float):
    return [
        item for item in products
        if item['stock'] == stock and item['price'] == price
    ]
 
@app.post('/products')
def create_product(product: Product):
    products.append(product.dict())
    return product