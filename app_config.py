from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware


# origins = [
#     "http://localhost:3001",
#     "https://localhost:3001",
#     "http://localhost:3000",
#     "https://localhost:3000",
#     "http://127.0.0.1:3000",
#     "https://127.0.0.1:3000",
#     "http://localhost",
#     "http://localhost:8080",
#     "https://61a9-77-37-227-80.ngrok-free.app"
# ]

app = FastAPI(default_response_class=ORJSONResponse)


app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )