from fastapi import FastAPI
from pydantic import BaseModel


item_master = {1: "Apple",
               2: "Mango",
               3: "Banana",
               4: "Grapes",
               5: "Orange"}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None               

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# 2nd page of application/URL/ end point of application
@app.get("/items")
async def items():
    return {"items": f"list of items{item_master}"}  

@app.get("/items/{item_id}")
async def get_item(item_id: int,  short: bool = False):
    if short == False:
        return  {"item": item_master[item_id]} 
    else:
        return {"item":"This is a long description"}     
            
@app.post("/items")
async def create_item(item: Item):
    return item.name


#No. of Endpoints = No. of functions
#get=read
#put=write

