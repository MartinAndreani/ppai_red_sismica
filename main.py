from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from test_front import eventos
from Interfaz.PantallaRegistrarResultadoDeRevisiónManual import PantallaRegistrarResultadoDeRevisiónManual

load_dotenv()

app = FastAPI()
pantalla = PantallaRegistrarResultadoDeRevisiónManual()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hola")
def leer_hola():
    return {"mensaje": "Hola desde FastAPI"}

@app.get("/api/eventos")
def get_eventos():
    return pantalla.habilitar(eventos)

@app.get("/api/eventos/datos-restantes")
def get_datos_restantes():
    return pantalla.getDatosRestantes()
    
@app.get("/api/eventos/{evento_id}/detalles")
def get_detalles_evento(evento_id: int):
    pantalla.seleccionarEventoSismico(evento_id)
    datos_restantes = pantalla.mostrarDatosEventoSismico()
    series_temporales = pantalla.mostrarSeriesTemporales()
    return {
        "datos_restantes": datos_restantes,
        "series_temporales": series_temporales
    }
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

