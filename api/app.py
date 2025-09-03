from fastapi import FastAPI
from api.routes import chatbot

app = FastAPI()

app.include_router(chatbot.router)
