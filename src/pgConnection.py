import psycopg2

def getHolding():
    conn = psycopg2.connect("dbname=mydb user=postgres password=xxxxx")
    cur = conn.cursor()
    cur.execute('select stock_code, quantity, bookcost from holding')
    holdings = cur.fetchall()

    for row in holdings:
        print('stock code = ', row[0])
        print('quantity = ', row[1])
        print('bookcost = ', row[2])

if __name__ == '__main__':

    getHolding()