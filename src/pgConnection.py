import psycopg2

def showdata():
    conn = psycopg2.connect("dbname=mydb user=postgres password=qwerty02")
    cur = conn.cursor()
    cur.execute('select stock_code, quantity from holding')
    holdings = cur.fetchall()

    for row in holdings:
        print('stock code = ', row[0])
        print('quantity = ', row[1])

if __name__ == '__main__':

    showdata()