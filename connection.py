import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import pymysql
from pandas import DataFrame
import random
from random import sample
import math

try:
    # This involved passwords specific to my database, I have uploaded a csv version instead in case anyone would want to use it
    cnx = mysql.connector.connect(user = 'root', password = '', host = 'localhost', database = 'anime')
    print ("Connection Established")

except mysql.connector.Error as err:
    print("Could not connect", err)


hostname= "localhost"
database= "anime"
username= "root"
password= ""



engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))
cursor = cnx.cursor(buffered=True)

new_anime = "SELECT DISTINCT English, Type, Aired, Episodes, Genres, Score FROM scraped_anime_table WHERE Genres != 'n'" #DISTINCT as table contains duplicates



cursor.execute(new_anime)
presented_data = pd.read_sql(new_anime, cnx)


english_names = presented_data['English']


random.seed(random.randint(0,300))
random_value = random.randint(0, english_names.shape[0] - 1) #Ensuring range not out of bounds
random_presented = english_names.iloc[random_value]
print(random_presented)

english_drop = random_presented 

print(english_drop.replace(" ", ""))



################################################################# HINT SECTION ##################################################


score_cleaned, score_garbage = presented_data['Score'][random_value].split('(')
score_cleaned = score_cleaned[0:5]


type_cleaned = presented_data['Type'][random_value]


aired_cleaned = presented_data['Aired'][random_value]


episodes_cleaned = presented_data['Episodes'][random_value]

genres_cleaned = presented_data['Genres'][random_value]


number_unique = {}

def count_letters(string):
   # Stores all distinct characters
    s = set(string)
 
    # Return the size of the set
    return len(s)

def unique_letter(string):

    pull_unique = set(string)

    return  list(pull_unique)

must_be_20_percent = math.ceil(((count_letters(english_drop.replace(" ", ""))) - 1) * 0.33)

random_letter = []

#GIVE 33% OF THE LETTERS AS A HINT and ensure they're unique
unique_number = random.sample(range(0, len(unique_letter(english_drop.replace(" ", "")))), must_be_20_percent)


for total_letters_given in unique_number:
    random_letter.append(unique_letter(english_drop.replace(" ", ""))[total_letters_given])

random_letter_as_String = ' '.join([str(elem) for elem in random_letter]) 
        
