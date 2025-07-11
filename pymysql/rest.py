
import requests
import csv
import json
import pymysql
from pymongo import MongoClient 
import pandas as pd

# REST API URL
API_URL = "https://jsonplaceholder.typicode.com/users"

# ---------- Step 1: Fetch API Data ----------
def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise HTTPError for bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# ---------- Step 2: Write to JSON File ----------
def write_to_json(data):
    try:
        with open("users.json", "w") as f:
            json.dump(data, f, indent=4)
        print("JSON file written successfully.")
    except Exception as e:
        print(f"Error writing JSON: {e}")

# ---------- Step 3: Write to CSV File ----------
def write_to_csv(data):
    try:
        keys = data[0].keys()
        with open("users.csv", "w", newline="") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print("CSV file written successfully.")
    except Exception as e:
        print(f"Error writing CSV: {e}")

# ---------- Step 4: Insert into MySQL ----------
def insert_into_mysql(data):
    connection=None
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Password@1",      # Your password
            database="emp" # Create DB and table before running
        )
        cursor = connection.cursor()
        for user in data:
            sql = """INSERT INTO users (id, name, username, email)
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (user['id'], user['name'], user['username'], user['email']))
        connection.commit()
        print(" Data inserted into MySQL successfully.")
    except pymysql.MySQLError as e:
        print(f"MySQL Error: {e}")
    finally:
        if connection:
            connection.close()

# ---------- Step 5: Insert into MongoDB ----------
def insert_into_mongodb(data):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["testdb"]
        collection = db["users"]
        collection.insert_many(data)
        print(" Data inserted into MongoDB successfully.")
    except Exception as e:
        print(f"MongoDB Error: {e}")

# ---------- Main Execution ----------
if __name__ == "__main__":
    users = fetch_data()
    if users:
        write_to_json(users)
        write_to_csv(users)
        insert_into_mysql(users)
        insert_into_mongodb(users)
