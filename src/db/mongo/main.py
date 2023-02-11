from sshtunnel import SSHTunnelForwarder
import pymongo
import random
from src.config.envs import SSH, SSH_CONFIG, MONGODB_CONFIG
from src.config.logger import logger




def connectMongoDB(database="test", collection="test"):
    """Connect to Mongo Database"""
    local_port = MONGODB_CONFIG["port"]
    tunnel = None

    # Check SSH config
    if SSH:
        while True:
            try:
                # SSH to server
                local_port = random.randint(27030, 28000)
                tunnel = SSHTunnelForwarder(
                    ssh_address_or_host=(SSH_CONFIG["host"], SSH_CONFIG["port"]),
                    ssh_username=SSH_CONFIG["username"],
                    ssh_password=SSH_CONFIG["password"],
                    remote_bind_address=("127.0.0.1", 3306),
                    local_bind_address=("127.0.0.1", local_port),
                )
                tunnel.start()
                break
            except Exception as e:
                logger.error(msg=e, error=e)

    # Connect to MongoDB
    client = pymongo.MongoClient(
        host=MONGODB_CONFIG["host"],
        port=local_port,
        username=MONGODB_CONFIG["username"],
        password=MONGODB_CONFIG["password"],
    )
    db = client[database]
    col = db[collection]
    return tunnel, col


def close(tunnel=None, collection=None):
    try:
        # Close Tunnel
        tunnel.close()
    except:
        pass

    try:
        # Close Collection
        collection.database.client.close()
    except:
        pass
