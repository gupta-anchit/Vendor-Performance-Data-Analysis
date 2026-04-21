import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logger = logging.getLogger("ingestion_db")
logger.setLevel(logging.DEBUG)
# file handler
file_handler = logging.FileHandler("Logs/ingestion_db.log", mode = "a")
file_handler.setLevel(logging.DEBUG)
# formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
file_handler.setFormatter(formatter)
# avoid duplicate logs
if not logger.handlers:
    logger.addHandler(file_handler)

engine = create_engine("sqlite:///inventory.db")

def ingest_db(df, table_name, engine):
    """this function will ingest the dataframe into the database table"""
    df.to_sql(table_name, con = engine, if_exists = "replace", index = False)

def load_raw_data():
    """this function will load the CSVs as dsataframes and ingest into database"""
    start = time.time()
    for file in os.listdir("Data"):
        if ".csv" in file:
            df = pd.read_csv("Data/" + file)
            logger.info(f"Ingesting {file} in database")
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60
    logger.info("Ingestion Complete")

    logger.info(f"\n Total Time Taken: {total_time} minutes")

if __name__ == '__main__':
    load_raw_data()