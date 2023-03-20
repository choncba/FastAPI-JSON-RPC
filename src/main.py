from fastapi import FastAPI, Request, Response
from jsonrpcserver import Result, Success, dispatch, method
# import uvicorn

app = FastAPI()


@method
def ping() -> Result:
    return Success("pong")

@method
def hola(name: str = None) -> Result:
    """
    Con Postman, POST a http://localhost:8000

    Body -> RAW: {"jsonrpc": "2.0", "method": "hola", "params": ["Luciano"], "id": 125}
    Respuesta: {"jsonrpc": "2.0", "result": "Hola Luciano", "id": 125}
    
    Body -> RAW: {"jsonrpc": "2.0", "method": "hola", "id": 125}
    Respuesta: {"jsonrpc": "2.0", "result": "Hola alguien", "id": 125}
    """
    return Success(f"Hola {name if name else 'alguien'}")


@app.post("/")
async def index(request: Request):
    return Response(dispatch(await request.body()))


# if __name__ == "__main__":
#     uvicorn.run(app, port=5000)