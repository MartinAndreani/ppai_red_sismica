from fastapi import FastAPI

ppai = FastAPI()

@ppai.get("/")
def home():
    return  {"HOLA MUNOD! "}