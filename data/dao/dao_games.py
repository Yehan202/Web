from data.modelo.juego import Juego
from data.database import database
from typing import Annotated

class DaoJuegos:
    
    def get_all(self,db) -> list[Juego]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM Juegos")

        equipos_en_db = cursor.fetchall()
        equipos : list[Juego]= list()
        for equipo in equipos_en_db:
            juego = Juego(equipo[0], equipo[1])
            equipos.append(juego)
        cursor.close()
        
        return equipos
    
    # def insert(self, db, nombre: str):
    #     cursor = db.cursor()
    #     sql = ("INSERT INTO Juegos (nombre) values (%s) ")
    #     data = (nombre,)
    #     cursor.execute(sql,data)
    #     # cursor.execute(f"INSERT INTO alumnos (nombre) VALUES ('{nombre}')")
    #     db.commit()
    #     cursor.close()

    # def delete(self, db, id: str):
    #     cursor = db.cursor()
    #     sql = ("DELETE FROM Juegos where id = (%s) ")
    #     data = (id,)
    #     cursor.execute(sql,data)
    #     # cursor.execute(f"INSERT INTO alumnos (nombre) VALUES ('{nombre}')")
    #     db.commit()
    #     cursor.close()