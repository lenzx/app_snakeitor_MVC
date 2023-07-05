import pymysql

class DB:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='snakeitor'
        )
        self.cursor = self.connect.cursor()
        

