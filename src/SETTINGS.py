import configparser

class CONFIGGER:
    def __init__(self,file_name):
        config = configparser.ConfigParser()

        config.read(file_name)

        self.database = config['database']['database']

        #print(f"Host: {host}, User: {user}, Password: {password}, Database: {database}")
