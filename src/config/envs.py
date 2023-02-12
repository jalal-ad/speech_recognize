import os
import json
from dotenv import load_dotenv


LOGGING_CONFIG = {}


"""Load Env variables"""
load_dotenv()


LOGGING_CONFIG = {
    "host": os.environ["logstash_host"],
    "port": int(os.environ["logstash_port"]),
    "logger_name": os.environ["logger_name"],
    "project": os.environ["project"],
    "logger_network": os.environ["logger_network"]
}


