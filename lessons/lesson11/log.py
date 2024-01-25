import logging


logging.basicConfig(level=logging.INFO,
                    filename='app.log',
                    filemode='a',
                    format='%(name)s %(asctime)s -[%(process)d, %(processName)s]  %(funcName)s - %(levelname)s - %(message)s')