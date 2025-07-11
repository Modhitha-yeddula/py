import requests
import csv
import json
import pymysql.connector
import pymongo
API_Users=url("https://jsonplaceholder.typicode.com/users")
user_json_data=[]
users_data=[]
for user in users:
    user_json_data.append('uid':users['id'])