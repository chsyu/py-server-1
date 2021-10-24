import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Hello World for Root Page"


@app.get("/products")
def products():
    return "THIS IS A PRODUCTS PAGE"

def get_product():
    ...

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)
