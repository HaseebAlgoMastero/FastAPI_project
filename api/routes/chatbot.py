from fastapi import APIRouter
from pydantic import BaseModel
from main import main 

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

# Request body model
class ChatRequest(BaseModel):
    query: str

@router.post("/")
def get_response(request: ChatRequest):
    response = main(request.query)
    print("DEBUG RESPONSE:", response)
    return {"query": request.query, "response": response}
