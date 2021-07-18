from core.pyba_logic import PybaLogic


class BooksLogicAudio(PybaLogic):
    def __init__(self):
        super().__init__()

    # get
    def getBooksByName(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_505461be12611e0.audio where nombre = '{id}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    # post
    def getBooksByName(self, name):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_505461be12611e0.pdf where nombre ='{name}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return []
