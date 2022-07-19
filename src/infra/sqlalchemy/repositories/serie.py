from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorySerie():
    def __init__(self, db: Session):
        self.db = db

    def create(self, serie: schemas.Serie):
        db_serie = models.Serie(title=serie.title,
                                    year=serie.year,
                                    gender=serie.gender,
                                    qtd_temp=serie.qtd_temp)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def listem(self):
        serie = self.db.query(models.Serie).all()
        return serie

    def get(self, serie_id: int):
        stmt = select(models.Serie).filter_by(id=serie_id)
        serie = self.db.execute(stmt).one()
        return serie

    def remove(self, serie_id):
        stmt = delete(models.Serie).where(models.Serie.id == serie_id)
        self.db.execute(stmt)
        self.db.commit()
