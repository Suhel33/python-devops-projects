from fastapi import FastAPI         # importing FastApi class
from routers import metrics_route, aws_route

app = FastAPI(
    title= "Internal DevOps Utilities API",
    description= "This is an Internal API Utilities Application for Monitoring metrics, AWS Usage, Log Analysis, etc.",
    version= "1.0.0",       # Sementic Versioning
    docs_url= "/docs",
    redoc_url="/redoc"
)

@app.get("/")       # decorator
def hello():
    """
        This is a hello API. Just for a testing
    """
    return {"message":"Hello Dosto, Thid is a DevOps Utilities API."}

app.include_router(metrics_route.router)
app.include_router(aws_route.router, prefix="/aws")