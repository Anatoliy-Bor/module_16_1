from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"msg":"Главная страница !"}

@app.get("/user/admin")
async def read_admin() -> dict:
    return {"msg":"Вы зашли как администратор !"}

@app.get("/user/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"msg":f"Вы вошли как пользователь № {user_id}"}

@app.get("/id")
async def tak_user(username: str, age: int) -> dict:
    return {"User": username, "Age": age}

