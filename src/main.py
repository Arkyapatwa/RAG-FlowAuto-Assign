from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    
    from routes import search
    
    app.include_router(search.router, prefix="/search", tags=["Search"])
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,  port=8000)