## pip install duckdb


#---------------------------------- Setting Up the DuckDB ------------------------------------------------#
import duckdb
import polars as pl
import pandas as pd
# Create a persistent database to store things 
dbcon = duckdb.connect("samhsa_data.db")

#--------------- Ingest Data into table ------------------------------------------------------------------#

file_path = '../../data/tedsa_puf_2015_2019.csv'
# Create a persistent database to store things 
dbcon = duckdb.connect("teds_raw_data.db")

# Creating Table teds_a_raw_2015_2019
dbcon.execute(f"""
    CREATE TABLE teds_a_raw_2015_2019 AS SELECT * FROM read_csv_auto('{file_path}')
""")

# Checking Result 
result = dbcon.execute("SELECT * FROM teds_a_raw_2015_2019 limit 10").fetchdf()
result.head()
