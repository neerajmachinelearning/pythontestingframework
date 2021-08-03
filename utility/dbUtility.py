import pymysql

from utility.credentialsUtility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        cred_object = CredentialsUtility()
        self.db_cred = cred_object.get_db_credentials()
        self.host = 'localhost'
        self.socket = 'socket address'  # Get these data from the dev or infra team


    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.db_cred['db_user'], password=self.db_cred['db_password'], unix_socket=self.socket)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)   # This gets db result in dictionary
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failled running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()
        return  rs_dict

    