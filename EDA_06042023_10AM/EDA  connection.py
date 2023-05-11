# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:18:19 2023

@author: seema
"""

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer # term frequency - inverse document frequncy is a numerical statistic that is intended to reflect how important a word is to document in a collecion or corpus
# from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from sqlalchemy import create_engine
#pip install pymysql
import pymysql
import mysql.connector as connector

# import Dataset 
anime = pd.read_csv(r"C:\Users\agila\OneDrive\Desktop\anime.csv")

# Database Connection

# Upload the Table into Database

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user = "root",# user
                               pw = "arjuna", # passwrd
                               db = "furniture1")) #database

anime.to_sql('anime', con = engine, if_exists = 'append', chunksize = 1000, index = False)


# Read the Table (data) from MySQL

cur.execute('SELECT * FROM anime')
df = cur.fetchall()

anime = pd.DataFrame(df)
anime = anime.rename({0 : 'anime_id'}, axis = 1)
anime = anime.rename({1 : 'name'}, axis = 1)
anime = anime.rename({2 : 'genre'}, axis = 1)
anime = anime.rename({3 : 'type'}, axis = 1)
anime = anime.rename({4 : 'episodes'}, axis = 1)
anime = anime.rename({5 : 'rating'}, axis = 1)
anime = anime.rename({6 : 'members'}, axis = 1)

# Check for Missing values
anime["genre"].isnull().sum() 

# Impute the Missing values in 'genre' column for a movie with 'General' category
anime["genre"] = anime["genre"].fillna("General")

# Create a Tfidf Vectorizer to remove all stop words

tfidf = TfidfVectorizer(stop_words = "english")   # taking stop words from tfidf vectorizer 

# Transform a count matrix to a normalized tf-idf representation
tfidf_matrix = tfidf.fit(anime.genre)   

# Save the Pipeline for tfidf matrix

joblib.dump(tfidf_matrix, 'matrix')

os.getcwd()

mat = joblib.load("matrix")

tfidf_matrix = mat.transform(anime.genre)

tfidf_