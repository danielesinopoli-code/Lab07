from UI.alert import AlertManager
from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass


    def get_all_epoc(self ):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore nel creare la connessione DB")
            return []

        cursor = cnx.cursor()
        query = """ SELECT DISTINCT epoca 
                    FROM artefatto 
                    ORDER BY epoca ASC """
        try:
            cursor.execute(query)
            for row



