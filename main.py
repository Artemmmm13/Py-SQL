# Artem Fedorchenko 223663IVSB
"""@author artfed"""
import sqlite3

DB_NAME = "artfed.db"


def create_tables():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS PROVIDER (
                            ID INT PRIMARY KEY AUTOINCREMENT NOT NULL,
                            ProviderName TEXT
                        )""")

        cur.execute(""" CREATE TABLE IF NOT EXISTS CANTEEN (
                    ID INT PRIMARY KEY AUTOINCREMENT NOT NULL,
                    ProviderID NULL,
                    Name_ TEXT NULL,
                    Location TEXT NULL,
                    time_open INT NULL,
                    time_closed INT NULL,
                    FOREIGN KEY (ProviderID) REFERENCES PROVIDER(ID)
                );""")
        conn.commit()


def insert_into_tables():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO PROVIDER (ProviderName) VALUES (?)", ("Rahva Toit",))
        cur.execute("INSERT INTO PROVIDER (ProviderName) VALUES (?)", ("Baltic Restaurants Estonia AS",))
        cur.execute("INSERT INTO PROVIDER (ProviderName) VALUES (?)", ("TTÜ Sport",))
        cur.execute("INSERT INTO PROVIDER (ProviderName) VALUES (?)", ("BiStop Kohvik OÜ",))

        canteens = [
            (4, "BiStop Kohvik", "Raja 4c", 930, 1600),
            (1, "Economics- and social science building canteen", "Akadeemia tee 3", 830, 1830),
            (1, "Library canteen", "Akadeemia tee 1/Ehitajate tee 7", 830, 1900),
            (2, "Main building Deli cafe", "Ehitajate tee 5, U01 building", 900, 1630),
            (2, "Main building Daily lunch restaurant", "Ehitajate tee 5, U01 building", 900, 1630),
            (1, "U06 building canteen", "UO6", 900, 1630),
            (2, "Natural Science building canteen", "Akadeemia tee 15, SCI building", 900, 1600),
            (2, "ICT building canteen", "Raja 15/Mäepealse 1", 900, 1600),
            (3, "Sports building canteen", "Männiliiva 7, S01 building", 1100, 2000),
        ]

        cur.executemany(
            "INSERT INTO CANTEEN (ProviderID, Name_, Location, time_open, time_closed) VALUES (?, ?, ?, ?, ?)",
            canteens)
        conn.commit()


def query_tables():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM CANTEEN WHERE time_open >= 900 AND time_closed <= 1620")
        result1 = cur.fetchall()
        print("Query 1 result:")
        print(result1)

        cur.execute("""SELECT CANTEEN.*, PROVIDER.ProviderName FROM CANTEEN
                          INNER JOIN PROVIDER ON CANTEEN.ProviderID = PROVIDER.ID
                          WHERE PROVIDER.ProviderName = 'Baltic Restaurants Estonia AS'""")
        result2 = cur.fetchall()
        print("\nQuery 2 result:")
        print(result2)


if __name__ == '__main__':
    create_tables()
    insert_into_tables()
    query_tables()
