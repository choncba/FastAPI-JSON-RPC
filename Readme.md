# JSON RPC Implementation example with FastAPI

https://www.jsonrpcserver.com/en/stable/index.html

## Install with pipenv

pipenv install jsonrpcserver "fastapi[all]"

## Run

pipenv run uvicorn main:app --reload

## Test

curl -X POST http://localhost:8000 -d '{"jsonrpc": "2.0", "method": "ping", "id": 1}'