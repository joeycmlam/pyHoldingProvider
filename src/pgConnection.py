import psycopg2

class dbConnection():
    conn = None

    def connectDb(self, dsn_info):
        self.conn = psycopg2.connect(dsn=dsn_info)


    def execSQL(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result

def main():
    print ('test')
    db = dbConnection()
    db.connectDb("dbname=mydb user=postgres password=xxxx")
    holdings = db.execSQL('select stock_code, quantity, bookcost from holding')
    for aHolding in holdings:
        print(aHolding)

if __name__ == '__main__':
    main()