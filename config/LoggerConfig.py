import logging

class LoggerConfig:
    def __init__(self, nombre_logger, nivel=logging.DEBUG, archivo_log=None):
        self.logger = logging.getLogger(nombre_logger)
        self.set_nivel(nivel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Crear y configurar el manejador de consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Si se proporciona un archivo de log, crear y configurar el manejador de archivo
        if archivo_log:
            file_handler = logging.FileHandler(archivo_log)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def set_nivel(self, nivel):
        self.logger.setLevel(nivel)

    def get_logger(self):
        return self.logger