from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/scripts/{filename}")
async def serve_scripts(filename: str):
    return FileResponse(f"scripts/{filename}")


@app.get("/assets/{filename}")
async def serve_assets(filename: str):
    return FileResponse(f"assets/{filename}")


@app.get("/styles/{filename}")
async def serve_styles(filename: str):
    return FileResponse(f"styles/{filename}")


@app.get("/")
async def serve_index():
    return FileResponse("views/index.html")


@app.get("/essays")
async def serve_essays():
    return FileResponse("views/essays.html")


@app.get("/photography")
async def serve_photography():
    return FileResponse("views/photography.html")


@app.get("/hobbies")
async def serve_hobbies():
    return FileResponse("views/hobbies.html")
