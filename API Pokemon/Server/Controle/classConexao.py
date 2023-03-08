from psycopg2 import connect, Error

class Conexao():
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        
    def querySelect(self, sql):
        try:
            con = connect(database=self.db, user=self.user, host=self.host, password=self.password)
            
            cursor = con.cursor()
            
            cursor.execute(sql)
            
            res = cursor.fetchall()
            
            cursor.close()
            
            con.close()
            return res            
        except Error as err:
            print(f"Error: {err}")
    
    def queryExecute(self, sql):
        con = connect(database=self.db, user=self.user, host=self.host, password=self.password)
            
        cursor = con.cursor()
        
        cursor.execute(sql)
        
        con.commit()
        
        cursor.close()
        
        con.close()