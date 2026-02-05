from fastapi import FastAPI

# create a FastAPI Instance
app = FastAPI(
    title="Food Vlog API",
    description="API for food vlogging platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)