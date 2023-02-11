import os
import json
from dotenv import load_dotenv


RMQ_CONFIG = {}
LOGGING_CONFIG = {}
SSH_CONFIG = {}
MONGODB_CONFIG = {}
MYSQL_CONFIG = {}


"""Load Env variables"""
load_dotenv()

SSH = os.environ.get("ssh", False) == "yes"
rabbitmq = os.environ.get("rabbitmq", False) == "yes"
logstash = os.environ.get("logstash", False) == "yes"
mongo = os.environ.get("mongo", False) == "yes"
mysql = os.environ.get("mysql", False) == "yes"
DEBUG = os.environ.get("debug", False) == "yes"

if rabbitmq:
    RMQ_CONFIG = {
        "host": os.environ["rabbitmq_host"],
        "port": int(os.environ["rabbitmq_port"]),
        "virtual_host": os.environ["rabbitmq_virtual_host"],
        "username": os.environ["rabbitmq_username"],
        "password": os.environ["rabbitmq_password"],
        "routing_keys": json.loads(os.environ["rabbitmq_routing_keys"]),
        "thread": int(os.environ["rabbitmq_thread"]),
        "heartbeat": int(os.environ["rabbitmq_heartbeat"]),
    }


if logstash:
    LOGGING_CONFIG = {
        "host": os.environ["logstash_host"],
        "port": int(os.environ["logstash_port"]),
        "logger_name": os.environ["logger_name"],
        "project": os.environ["project"],
        "logger_network": os.environ["logger_network"]
    }


if SSH:
    SSH_CONFIG = {
        "host": os.environ["ssh_host"],
        "port": int(os.environ["ssh_port"]),
        "username": os.environ["ssh_username"],
        "password": os.environ["ssh_password"],
    }


if mongo:
    MONGODB_CONFIG = {
        "host": os.environ["mongo_host"],
        "port": int(os.environ["mongo_port"]),
        "username": os.environ["mongo_username"],
        "password": os.environ["mongo_password"],
    }


if mysql:
    MYSQL_CONFIG = {
        "host": os.environ["mysql_host"],
        "port": int(os.environ["mysql_port"]),
        "username": os.environ["mysql_username"],
        "password": os.environ["mysql_password"],
        "database": os.environ["mysql_database"],
    }
