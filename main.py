from fastapi import FastAPI
from matcher import Matcher
from schemas import UserRequest

app = FastAPI()
matcher = Matcher()

@app.post("/join")
def join_waitlist(user: UserRequest):
    result = matcher.add_user(user)
    return result

@app.get("/")
def home():
    return {"message": "BOGO Buddy backend is running!"}
