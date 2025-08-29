from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My API with Pydantic")

class Product(BaseModel):
    name: str
    price: int
    available: bool = True
   
   
products = []

@app.get("/")
def hello_world() -> dict:
    return {"message": "API with Pydantic!"}

@app.post("/products")
def create_product(product: Product) -> dict:
    product_dict = product.dict()
    product_dict["id"] = len(products) + 1
    products.append(product_dict)
    return {"message": "Product created", "product": product_dict}

# Endpoint para ver todos los productos
@app.get("/products")
def get_products() -> dict:
    return {"products": products, "total": len(products)}


@app.get("/info")
def info() -> dict:
    return {"api": "FastAPI", "week": 1, "status": "running"}

# NUEVO: Endpoint POST con Pydantic

# NUEVO: Endpoint personalizado (solo si hay tiempo)
@app.get("/greeting/{name}")
def greet_user(name: str) -> dict:
    return {"greeting": f"¡Hola {name}!"}

@app.get("/my-profile")
def my_profile() -> dict:
    return {
        "name": "Wilson Ontibón",
        "bootcamp": "FastAPI",
        "week": 1,
        "date": "2025",
        "likes_fastapi": True
    }
    
@app.get("/calculate/{num1}/{num2}")
def calculate(num1: int, num2: int) -> dict:
    result = num1 + num2
    return {"result": result, "operation": "sum"}

@app.get("/fruits")
def get_fruits() -> list[str]:
    return ["apple", "banana", "cherry"]

@app.get("/cosa")
def get_cosa() -> list[str]:
    return ["Coming up", "Say Say Say", "yeayeayea"]