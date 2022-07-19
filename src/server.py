from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Serie
from src.infra.sqlalchemy.config.database import get_db, start_db
from src.infra.sqlalchemy.repositories.serie import RepositorySerie

start_db()

app = FastAPI()


@app.post('/series')
def create_serie(serie: Serie, db: Session = Depends(get_db)):
    serie_created = RepositorySerie(db).create(serie)
    return serie_created

@app.get('/series')
def listem_serie(db: Session = Depends(get_db)):
    serie = RepositorySerie(db).listem()
    return serie

@app.get('/series/{serie_id}')
def getOne(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorySerie(db).get(serie_id)
    return serie

@app.delete('/series/{serie_id}')
def deleteSerie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorySerie(db).remove(serie_id)
    return {'msg': 'Serie removida com sucesso.'}
