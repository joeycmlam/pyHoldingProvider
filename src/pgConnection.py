import psycopg2
import yaml

class dbConnection():
    conn = None
    dbname = ''
    dbuser = ''
    dbpassword = ''
    config_file = '../resource/config.yaml'
    config = None

    def __init__(self):
        self.conn = None

        try:
            config = open(self.config_file)
            parsed_yaml_file = yaml.load(config, Loader=yaml.FullLoader)
            self.dbname = parsed_yaml_file['database']['postgre']['dbname']
            self.dbuser = parsed_yaml_file['database']['postgre']['user']
            self.dbpassword = parsed_yaml_file['database']['postgre']['password']
            dnsinfo = 'dbname=' + self.dbname + ' user=' + self.dbuser + ' password=' + self.dbpassword
            self.conn = psycopg2.connect(dsn= dnsinfo)
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


