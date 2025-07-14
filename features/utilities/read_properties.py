import configparser

config = configparser.ConfigParser()
config.read('./features/data/config.ini')

class ReadConfig():

    @staticmethod
    def get_app_url():
        """
        Get the application URL from the configuration file.
        :return: The application URL.
        """
        return config.get('common','base_url')
    
    @staticmethod
    def get_implicit_wait():
        """
        Get the implicit wait time from the configuration file.
        :return: The implicit wait time in seconds.
        """
        return config.get('common','implicit_wait')
