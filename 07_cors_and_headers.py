from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # or ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/public")
def public_endpoint():
    return {"message": "This route is accessible from any frontend."}

@app.get("/with-headers")
def custom_headers(response: Response):
    response.headers["X-App-Version"] = "1.0.3"
    response.headers["X-Custom-Info"] = "FastAPI-Rocks"
    return {"message": "Headers added successfully."}
