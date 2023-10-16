from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.configuration.mongodb_operations import MongoOperations

# if __name__ == "__main__":
#     mongo = MongoDBClient()
#     print("collection name:",mongo.database.list_collection_names())
#     #print(f"{mongo.database.list_connection_names()}")

if __name__ == "__main__":
    db_client = MongoOperations()
    # database_name = "sensor"
    # collection_name = "sensor_data"  
    # csv_file_path = r"sensor_csv_file.csv"

    db_client.create_database()
    db_client.create_collection()
    db_client.upload_csv_to_collection()