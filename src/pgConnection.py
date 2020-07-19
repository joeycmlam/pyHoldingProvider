import psycopg2

class dbConnection():
    conn = None
    dsn = ''

    def __init__(self):
        self.conn = None

        try:
            self.dns = 'dbname=mydb user=postgres password=xxxx'
            self.conn = psycopg2.connect(dsn=self.dns)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def execSQL(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return result


    def disconnect(self):
        self.conn.close()


def main():
    print ('test')
    db = dbConnection()
    holdings = db.execSQL('select stock_code, quantity, bookcost from holding')
    for aHolding in holdings:
        print(aHolding)
    db.disconnect()

if __name__ == '__main__':
    main()