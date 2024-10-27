from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///fuel_station.db')

Base = declarative_base()

class FuelStation(Base):
    __tablename__ = 'fuel_stations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

Base.metadata.create_all(engine)

fuel_station = FuelStation(name='АЗС №1', address='ул. Пушкина, 10')
session = session(bind=engine)
session.add(fuel_station)
session.commit()

query = session.query(FuelStation).filter_by(name='АЗС №1')
result = query.first()
print(result.name, result.address)
