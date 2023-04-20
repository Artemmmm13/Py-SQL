# Artem Fedorchenko 223663IVSB
"""@author artfed"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import time

engine = create_engine('sqlite:///artfed.db', echo=True)
Base = declarative_base()


class Provider(Base):
    __tablename__ = 'PROVIDER'

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ProviderName = Column(String)


class Canteen(Base):
    __tablename__ = 'CANTEEN'

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ProviderID = Column(Integer, ForeignKey('PROVIDER.ID'))
    Name_ = Column(String)
    Location = Column(String)
    time_open = Column(Time)
    time_closed = Column(Time)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def insert_and_query_tables():
    try:
        time_obj_1 = time(hour=8, minute=30)
        time_obj_2 = time(hour=9, minute=0)
        time_obj_3 = time(hour=18, minute=30)
        time_obj_4 = time(hour=16, minute=0)
        time_obj_5 = time(hour=16, minute=30)
        time_obj_6 = time(hour=11, minute=0)
        time_obj_7 = time(hour=20, minute=0)
        time_obj_8 = time(hour=9, minute=30)
        time_obj_9 = time(hour=19, minute=0)
        time_obj_10 = time(hour=16, minute=20)
        provider1 = Provider(ProviderName='Rahva Toit')
        session.add(provider1)

        provider2 = Provider(ProviderName='Baltic Restaurants Estonia AS')
        session.add(provider2)

        provider3 = Provider(ProviderName='TTÜ Sport')
        session.add(provider3)

        provider4 = Provider(ProviderName='BiStop Kohvik OÜ')
        session.add(provider4)

        canteen1 = Canteen(ProviderID=4, Name_='BiStop Kohvik', Location='Raja 4c', time_open=time_obj_8, time_closed=time_obj_4)
        session.add(canteen1)

        list_canteens = [
            Canteen(ProviderID=1, Name_='Economics- and social science building canteen', Location='Akadeemia tee 3',
                    time_open=time_obj_1, time_closed=time_obj_3),
            Canteen(ProviderID=1, Name_='Library canteen', Location='Akadeemia tee 1/Ehitajate tee 7', time_open=time_obj_1,
                    time_closed=time_obj_9),
            Canteen(ProviderID=2, Name_='Main building Deli cafe', Location='Ehitajate tee 5, U01 building',
                    time_open=time_obj_2,
                    time_closed=time_obj_4),
            Canteen(ProviderID=2, Name_='Main building Daily lunch restaurant',
                    Location='Ehitajate tee 5, U01 building',
                    time_open=time_obj_2, time_closed=time_obj_5),
            Canteen(ProviderID=1, Name_='U06 building canteen', Location='UO6', time_open=time_obj_2, time_closed=time_obj_5),
            Canteen(ProviderID=2, Name_='Natural Science building canteen', Location='Akadeemia tee 15, SCI building',
                    time_open=time_obj_2, time_closed=time_obj_4),
            Canteen(ProviderID=2, Name_='ICT building canteen', Location='Raja 15/Mäepealse 1', time_open=time_obj_2,
                    time_closed=time_obj_4),
            Canteen(ProviderID=3, Name_='Sports building canteen', Location='Männiliiva 7, S01 building',
                    time_open=time_obj_6,
                    time_closed=time_obj_7)
        ]
        session.add_all(list_canteens)

        result1 = session.query(Canteen).filter(Canteen.time_open >= time_obj_2, Canteen.time_closed <= time_obj_10).all()
        print(result1)
        print("\n")

        result2 = session.query(Canteen).join(Provider).filter(
            Provider.ProviderName == 'Baltic Restaurants Estonia AS').all()
        print(result2)

        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Connection to DB failed", e)
    finally:
        session.close()


if __name__ == '__main__':
    insert_and_query_tables()
