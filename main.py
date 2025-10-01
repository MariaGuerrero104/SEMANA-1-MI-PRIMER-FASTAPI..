from fastapi import FastAPI

app = FastAPI(title="Semana 1 - API Básica")

@app.get("/")
def root():
    return {"message": "Hola Mundo desde la Semana 1 🚀"}

@app.get("/hola/{nombre}")
def saludar(nombre: str):
    return {"message": f"Hola {nombre}, bienvenido a la Semana 1 😎"}
