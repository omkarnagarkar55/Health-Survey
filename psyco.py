import psycopg2 as pg
class Data():
    email=''
    height=0
    def __init__(self,email,height,weight,bmi):
        self.email=email
        self.height=height
        self.weight=weight
    
    def create(self):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS first(id SERIAL PRIMARY KEY,email_ VARCHAR(125),height_ REAL,weight_ REAL)")
        conn.commit()
        conn.close()
    
    def create2(self):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS first2(id SERIAL references first(id),bmi REAL)")
        conn.commit()
        conn.close()     
        
    def insert(self,email,height,weight):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("INSERT INTO first (email_,height_,weight_) VALUES(%s,%s,%s)",(email,str(height),str(weight)))
        conn.commit()
        conn.close() 
        
    def insert2(self,bmi):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("INSERT INTO first2(bmi) VALUES(%s)",(bmi,))
        conn.commit()
        conn.close()  
        
    def count(self,element):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("SELECT COUNT(email_) FROM first WHERE email_=%s ",(element,))
        c=cur.fetchall()
        conn.close()
        return c
        
    def average(self):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("SELECT AVG(height_) FROM first")
        rows=cur.fetchall()
        conn.close()
        return rows
    
    def countAll(self):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("SELECT COUNT(id) FROM first")
        c=cur.fetchall()
        conn.close()
        return c
    
    def delete(self,email):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("DELETE FROM first WHERE email_=%s",(email,))
        conn.commit()
        conn.close() 
        
    def Analysis(self):
        conn=pg.connect("dbname='psyco' user='postgres' password='postgres123' host='localhost'")
        cur=conn.cursor()
        cur.execute("select f.id,weight_,height_,bmi from first f,first2 f2 where f.id=f2.id")
        c=cur.fetchall()
        conn.close()
        return c
