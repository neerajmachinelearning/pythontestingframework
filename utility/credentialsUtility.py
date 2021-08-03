import os

class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')  # DB_USER should be added as the environment variable
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("Data base credentials DB_USER and DB_PASSWORD must be in env variable")
        else:
            return {'db_user': db_user, 'db_password': db_password}


    @staticmethod
    def get_api_keys():
        api_key = os.environ.get('API_KEY')
        api_secrete = os.environ.get('API_SECRETE')

        if not api_key or not api_secrete:
            raise Exception("API credentials API_KEY and API_SECRETE must be in env variable")
        else:
            return {'api_key': api_key, 'api_secrete': api_secrete}
