from fastapi import FastAPI, Depends
from routers import category, brands, specifications, products


app = FastAPI()
app.include_router(category.router)
app.include_router(brands.router)
app.include_router(specifications.router)
app.include_router(products.router)
