from fastapi import FastAPI, Depends
from routers import category, brands


app = FastAPI()
app.include_router(category.router)
app.include_router(brands.router)
