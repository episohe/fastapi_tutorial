import uvicorn
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

class UserLevel(str, Enum):
    a = "a"
    b = "b"

@app.get("/users")
def get_users(grade: UserLevel = UserLevel.a):
    return {"grade": grade}


# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)