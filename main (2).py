
from database import SessionLocal, engine, test_connection


# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
