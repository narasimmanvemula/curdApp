from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

users = []

class Login(BaseModel):
    emailid : str
    password : str


# create operation
@app.post("/login")
def add_login(data: Login):

    for user in users:

        if user["emailid"] == data.emailid and user["password"] == data.password:

            return {
                "message": "Login successful"
            }

    return {
        "message": "Invalid email or password"
    }
       
    

# create operation
@app.post("/sinup")
def add_sinup(sinup: Login): #(variable name : class name)
    users.append(sinup)
    return{
        "message":"sinup successfully completed",
        "user":users
    }







