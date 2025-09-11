import logging
import os

from utils import Constantes


class SimpleLogger:
    def __init__(
        self,
        file_name: str = None,
        log_name: str = None,
        level: int = logging.INFO,
    ) -> None:
        """Inicializa el logger.

        Args:
            file_name (str, optional): Si se proporciona, el logger
                escribirá en este archivo. Defaults to None.
            log_name (str, optional): Si se proporciona, será el nombre
                en el log. Defaults to None.
            level (int, optional): Si se proporciona, el nivel mínimo a
                registrar en el log. Defaults to logging.INFO.
        """
        # En caso no se elija la ruta del archivo .log
        if file_name is None:
            file_name = f"{Constantes.ruta_log}/app.log"
        # Obtiene el nombre del archivo actual sin la extensión .py
        if log_name is None or len(log_name) < 1:
            try:
                log_name = os.path.splitext(os.path.basename(__file__))[0]
            except NameError:
                log_name = "notebook"

        # Obtiene o crea un logger con el nombre dado
        self.logger = logging.getLogger(log_name)
        # Establece el nivel de log mínimo a registrar
        self.logger.setLevel(level)

        # Crea un formateador (determina cómo se mostrarán los mensajes)
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        datefmt = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

        # Crea un FileHandler para escribir en un archivo
        handler = logging.FileHandler(file_name, encoding="utf-8")
        # Asigna el formateador al manejador
        handler.setFormatter(formatter)
        # Agrega el manejador al logger
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)

    def exception(self, message: str) -> None:
        self.logger.exception(message)
