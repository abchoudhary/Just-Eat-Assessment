import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


# Reading common values stored in config.ini file using below methods
class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_zipcode():
        zipcode = config.get('common info', 'zipcode')
        return zipcode
