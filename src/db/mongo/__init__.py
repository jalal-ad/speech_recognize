from src.db.mongo.main import connectMongoDB, close


class Mongo:
    connectMongoDB = connectMongoDB
    close = close
