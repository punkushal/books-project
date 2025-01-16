from typing import Annotated
from fastapi import Depends, FastAPI
from database import engine, sessionLocal
from sqlalchemy.orm import Session
import models
app = FastAPI()

models.Base.metadata.create_all(bind= engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def get_all(db : Annotated[Session, Depends(get_db)]):
    return db.query(models.Todos).all()
