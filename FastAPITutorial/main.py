from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Auth API", description="Simple Sign In / Sign Up API")

# In-memory database
users = {}

# Models
class Signup(BaseModel):
    username: str
    password: str
    email: str

class Login(BaseModel):
    username: str
    password: str

# Root
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Auth System"}

# Sign Up
@app.post("/signup")
def signup(user: Signup):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.username] = user
    return {"message": "User registered successfully"}

# Sign In
@app.post("/signin")
def signin(user: Login):
    if user.username not in users or users[user.username].password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

# Get User Details
@app.get("/user/{username}")
def get_user(username: str):
    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    u = users[username]
    return {
        "username": u.username,
        "email": u.email
    }
