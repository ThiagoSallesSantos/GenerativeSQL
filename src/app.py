## Description: Main application file for FastAPI

from fastapi import FastAPI

from src.routes import *

app = FastAPI()

## Include routes
app.include_router(database.router)
app.include_router(generate.router)
