import sqlite3
import psycopg2
DB_PATH = "postgresql://neondb_owner:npg_3QHYp9nzvjDy@ep-orange-firefly-bbmzudui-pooler.c-15.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn

    