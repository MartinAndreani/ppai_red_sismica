
# Red Sismica de PPAI

## Para inicializar el proyecto tiene que ejecutar el siguiente comando:

### 1. Clonar el Repositorio
```bash
  git clone https://github.com/MartinAndreani/ppai_red_sismica.git
```
### 2. Pararse dentro del directorio principal (ya teniendo python instalado) y ejecutar el siguiente comando para crear un entorno virtual:
```bash 
  python -m venv env
```
### 3. Activar el entorno virtual:
```bash
  source env/Scripts/activate
```
### 4. Instalar librerias necesarias:
```bash
  pip install uvicorn
```
```bash
  pip install fastapi
```
```bash
  pip install dotenv
```
### 4. Iniciar Proyecto
```bash
  uvicorn main:app
```