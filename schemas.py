# schemas.py

from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    email: str
    product: str
    
class MatchResponse(BaseModel):
    user1: str
    user2: str
    product: str


