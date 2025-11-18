from sqlalchemy import Column, Integer, String, Date
from db.database import Base  # ← Importamos Base do database.py

class Laureate(Base):
    __tablename__ = 'laureates'

    id = Column(Integer, primary_key=True)
    gender = Column(String(10))  # Female or Male.
    died_country = Column(String(100))
    born_city = Column(String(100))
    firstname = Column(String(100))
    lastname = Column(String(100))
    born = Column(Date)  # Data de nascimento.
    death = Column(Date)  # Data de morte.

    def __repr__(self):
        return f"<Laureate(name='{self.firstname} {self.lastname}', gender='{self.gender}')>"