import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import pymysql
from pandas import DataFrame
import random
import time

try:
    # This involved passwords specific to my database, I have uploaded a csv version instead in case anyone would want to use it
    cnx = mysql.connector.connect(user = '', password = '', host = '', database = '')
    print ("Connection Established")

except mysql.connector.Error as err:
    print("Could not connect", err)


hostname= "localhost"
database= "anime"
username= "root"
password= "Maximum60!"



engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))
cursor = cnx.cursor(buffered=True)

new_anime = "SELECT DISTINCT English, Type, Aired, Episodes, Score FROM scraped_anime_table" #DISTINCT as table contains duplicates


cursor.execute(new_anime)
presented_data = pd.read_sql(new_anime, cnx)


english_names = presented_data['English']


random.seed(random.randint(0,300))
random_value = random.randint(0, english_names.shape[0] - 1)
random_presented = english_names.iloc[random_value]
print(random_presented)

english_drop = random_presented.strip('English    ') ##clean up the garbage attached
#name_drop = english_drop.split(' Name:')[0]


################################################################# HINT SECTION ##################################################


score_cleaned, score_garbage = presented_data['Score'][random_value].split('(')
score_cleaned = score_cleaned[0:5]


type_cleaned = presented_data['Type'][random_value]


aired_cleaned = presented_data['Aired'][random_value]


episodes_cleaned = presented_data['Episodes'][random_value]

random_letter = english_drop[random.randint(0, len(english_drop))]
print(random_letter)

