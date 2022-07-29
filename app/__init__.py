from fastapi import FastAPI

from app.api import auth_router, book_router

app = FastAPI()
sub_app = FastAPI()

sub_app.include_router(auth_router)
sub_app.include_router(book_router)

app.mount('/api', sub_app)
