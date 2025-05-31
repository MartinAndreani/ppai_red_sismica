from fastapi import FastAPI, Request
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

@app.post("/api/eventos/accion")
async def post_evento_accion(request: Request):
    data = await request.json()
    evento_id = data.get("id")
    nuevo_estado = data.get("estado")
    if evento_id is None or not nuevo_estado:
        return {"mensaje": "Faltan datos para procesar la acción."}
    pantalla.seleccionarEventoSismico(evento_id)
    pantalla.seleccionarResultadoRevisionManual(nuevo_estado)
    return {"mensaje": f"Estado '{nuevo_estado}' aplicado al evento {evento_id}"}

@app.get("/api/test/eventos-todos")
def get_todos_los_eventos():
    eventos_info = []
    for evento in eventos:
        # Obtener el estado actual (último cambio de estado)
        estado_actual = None
        if hasattr(evento, "cambiosEstado") and evento.cambiosEstado:
            ultimo_cambio = evento.cambiosEstado[-1]
            if ultimo_cambio.estado is not None:
                estado_actual = ultimo_cambio.estado.nombre
            else:
                estado_actual = None
        evento_dict = {
            "id": getattr(evento, "id", None),
            "fechaHoraOcurrencia": str(getattr(evento, "fechaHoraOcurrencia", "")),
            "valorMagnitud": getattr(evento, "valorMagnitud", None),
            "latitudHipocentro": getattr(evento, "latitudHipocentro", None),
            "longitudHipocentro": getattr(evento, "longitudHipocentro", None),
            "latitudEpicentro": getattr(evento, "latitudEpicentro", None),
            "longitudEpicentro": getattr(evento, "longitudEpicentro", None),
            "estado_actual": estado_actual,
            "cambios_estado": [
                {
                    "nombre": cambio.estado.nombre if cambio.estado else None,
                    "ambito": cambio.estado.ambito if cambio.estado else None,
                    "fecha_inicio": str(cambio.fechaHoraInicio),
                    "fecha_fin": str(cambio.fechaHoraFin)
                }
                for cambio in getattr(evento, "cambiosEstado", [])
            ]
        }
        eventos_info.append(evento_dict)
    return eventos_info


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

