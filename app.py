from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://www.olanrewajusholarin.com/"],
    allow_methods = ["*"],
    allow_credentials = True,
    allow_headers = ["*"]
)

@app.get("/")
def get_compliment():
    with open("compliments.json", "r") as file:
        file_data = json.load(file)
        compliment: str = random.choice(file_data).strip()
        return {"message": f"Heyy Tomisin, {compliment}"}
