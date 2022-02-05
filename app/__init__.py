from fastapi import FastAPI

from app.api import auth_router, book_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(book_router)
