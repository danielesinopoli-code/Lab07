from audioop import error
from dataclasses import dataclass
from UI.alert import AlertManager
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


    def get_all_museum(self ):

        cnx=ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore nel creare la connessione DB")
            return None

        cursor = cnx.cursor(dictionary=True)
        query=""" SELECT * 
                  FROM museo
                  ORDER BY name ASC """

        try:
            lst_musei= []
            cursor.execute(query)
            for row in cursor:
                lst_musei.append(Museo(row))
            cursor.close()
            cnx.close()
            return lst_musei
        except error as e:
            print(f"Errore DAO =  {e}")




