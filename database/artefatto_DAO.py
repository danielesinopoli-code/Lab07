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


    def get_all_epoche(self ):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore nel creare la connessione DB")
            return []

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT epoca FROM artefatto WHERE epoca IS NOT NULL ORDER BY epoca ASC;"""
        try:
            lst_epoche = []
            cursor.execute(query)
            for row in cursor:
               lst_epoche.append(row["epoca"])

            cursor.close()
            cnx.close()
            return lst_epoche
        except Exception  :
            print("Errore nel DAO")

    def get_artefatti_filtrati(self, nome_museo, nome_epoca):

        conn = ConnessioneDB.get_connection()
        if conn is None:
            print("Errore! Impossibile connettersi al database.")
            return []

        cursor = conn.cursor(dictionary=True)


        query = """
            SELECT a.* FROM artefatto a JOIN museo m ON a.id_museo = m.id
            WHERE m.nome = COALESCE(%s, m.nome)
              AND a.epoca = COALESCE(%s, a.epoca)
            
        """

        try:

            cursor.execute(query, (nome_museo, nome_epoca))
            result = []
            for row in cursor:

                result.append(Artefatto(**row))
            return result
        except Exception as e:
            print(f"Errore DAO (get_artefatti_filtrati): {e}")
            return []
        finally:
            cursor.close()
            conn.close()




