"""Logging"""
from inspect import currentframe
import logging
import logstash
from src.config.envs import LOGGING_CONFIG, DEBUG


class Logger:
    def __init__(self, file_name, logger_name, project, log_type=None):
        self.logger = logging.getLogger(f"{logger_name}_{file_name}")
        self.logger.setLevel(logging.DEBUG)

        # Save on file
        handler = logging.FileHandler(f"logs/{file_name}.log")
        # Logging format
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.information = {"project": project, "type": log_type}


    def _lin_number(self):
        cf = currentframe()
        return cf.f_back.f_back.f_back.f_lineno

    def _path(self):
        cf = currentframe()
        return cf.f_back.f_back.f_back.f_code.co_filename

    def handle_info(self, info, error=None, pid=None):
        if info:
            info.update(self.information)
        else:
            info = self.information

        if pid:
            info["pid"] = pid

        info["lin_number"] = self._lin_number()
        info["path"] = self._path()
        if error:
            info["lin_error"] = error.__traceback__.tb_lineno
            info["error"] = str(error)

        return info

    def debug(self, msg=None, info=None, error=None, pid=None):
        info = self.handle_info(info=info, error=error, pid=pid)
        self.logger.debug(msg=msg, extra=info, exc_info=False)

    def info(self, msg=None, info=None, error=None, pid=None):
        info = self.handle_info(info=info, error=error, pid=pid)
        self.logger.info(msg=msg, extra=info, exc_info=False)

    def error(self, msg=None, info=None, error=None, pid=None):
        info = self.handle_info(info=info, error=error, pid=pid)
        self.logger.error(msg=msg, extra=info, exc_info=False)



# App Logger
logger = Logger(
    file_name="sys",
    logger_name=f"{LOGGING_CONFIG['project']}_sys",
    project=LOGGING_CONFIG["project"],
    log_type="app_log",
)
# # Result Logger
result_logger = Logger(
    file_name="result",
    logger_name=f"{LOGGING_CONFIG['project']}_result",
    project=LOGGING_CONFIG["project"],
    log_type="result",
)
