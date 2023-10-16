from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging

# def text_exception():
#     try:
#         logging.info("we are divide 1 by zero")
#         x=1/0
#     except Exception as e:
#         raise SensorException(e,sys)
    
# if __name__ == '__main__':
#     mongodb_client =MongoDBClient()
#     print("collection name:",mongodb_client.database.list_collection_names())
#     # try:
#     #     text_exception()
#     # except Exception as e:
#     #     print(e)
#     # mongodb_client = MongoDBClient()
#     # print("collection name:",mongodb_client.database.list_collection_names())


# if __name__ == '__main__':
