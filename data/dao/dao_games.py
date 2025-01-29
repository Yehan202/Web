from data.modelo.juego import Juego
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
    
    def insert(self, db, nombre: str):
        cursor = db.cursor()
        
        # Get the last id
        cursor.execute("SELECT MAX(id) FROM Juegos")
        last_id = cursor.fetchone()[0]
        new_id = last_id + 1 if last_id is not None else 1
        
        # Insert the new record with the new id
        sql = ("INSERT INTO Juegos (id, nombre) values (%s, %s)")
        data = (new_id, nombre)
        cursor.execute(sql, data)
        db.commit() 
        cursor.close()

    def delete(self, db, id: str):
        cursor = db.cursor()
        sql = ("DELETE FROM Juegos where id = (%s) ")
        data = (id,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO alumnos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()