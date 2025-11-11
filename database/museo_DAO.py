
from dataclasses import dataclass

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""
@dataclass
class MuseoDAO:
    def __init__(self):
        pass


    def get_all_musei(self ):

        cnx=ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore nel creare la connessione DB")
            return None

        cursor = cnx.cursor(dictionary=True)
        query=""" SELECT * 
                  FROM museo
                  ORDER BY nome ASC """

        try:
            lst_musei= []
            cursor.execute(query)
            for row in cursor:
                lst_musei.append(Museo(**row))
            cursor.close()
            cnx.close()
            return lst_musei
        except Exception as e:
            print(f"Errore DAO =  {e}")




