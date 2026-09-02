import psycopg2
from dotenv import load_dotenv
import os

load_dotenv("variaveis.env")


def get_connect_oltp():
    conn = psycopg2.connect(
        host=os.getenv("host"),
        port=os.getenv("port"),
        database=os.getenv("database"),
        user=os.getenv("user"),
        password=os.getenv("password")
    )
    return conn

def get_connect_dw():
    conn = psycopg2.connect(
        host=os.getenv("host"),
        port=os.getenv("port"),
        database=os.getenv("database2"),
        user=os.getenv("user"),
        password=os.getenv("password")
    )
    return conn
