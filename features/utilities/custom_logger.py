import logging

class LogGen:

    @staticmethod
    def log_gentest():
        """
        This method sets up the logging configuration for the application.
        It logs messages to a file named 'automation.log' in the 'logs' directory.
        """
        logging.basicConfig(
            filename="./logs/automation.log",
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger