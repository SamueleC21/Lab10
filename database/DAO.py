from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select *
                    from country c  """

        cursor.execute(query)

        for row in cursor:
            res.append(Country(**row))
            # res.append(ArtObject(object_id=row["object_id"], ...))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getNodes2(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        res = []
        query = """select c.state1no 
                    from contiguity c 
                    where year <= %s
                    union
                    select c2.state2no 
                    from contiguity c2
                    where year <= %s"""

        cursor.execute(query, (anno, anno, ))

        return cursor.fetchall()



    @staticmethod
    def getEdges(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        res = []
        query = """select c.state1no, c.state2no 
                    from contiguity c 
                    where c.conttype = 1
                    and year < %s """

        cursor.execute(query, (anno, ))

        for row in cursor:
            res.append(row)
            # res.append(ArtObject(object_id=row["object_id"], ...))

        cursor.close()
        conn.close()
        return res
