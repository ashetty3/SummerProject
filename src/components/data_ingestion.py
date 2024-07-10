## pip install duckdb


#---------------------------------- Setting Up the DuckDB ------------------------------------------------#
import duckdb
#import ibis

# Connect to the DuckDB database
dbcon = duckdb.connect('samhsa_data.db')
#con = ibis.duckdb.connect('samhsa_data.db')

#--------------- Ingest Data into table ------------------------------------------------------------------#

file_path = 'data/tedsa_puf_2015_2019.csv'

# Creating Raw Table teds_a_raw_2015_2019
dbcon.execute(f"""
    CREATE TABLE IF NOT EXISTS teds_a_raw_2015_2019 AS SELECT * FROM read_csv_auto('{file_path}')
""")

# Checking Result 
#result = dbcon.execute("SELECT * FROM teds_a_raw_2015_2019 limit 10").fetchdf()
#result.head()


# Queries to create other tables

create_demographics = '''
CREATE TABLE IF NOT EXISTS Demographics AS
SELECT
    CASEID,
    ADMYR,
    AGE,
    GENDER,
    RACE,
    ETHNIC,
    MARSTAT,
    EDUC,
    PREG,
    VET,
    STFIPS,
    CBSA2010,
    REGION,
    DIVISION
FROM teds_a_raw_2015_2019;
'''

create_employment_details = '''
CREATE TABLE IF NOT EXISTS EmploymentDetails AS
SELECT
    CASEID,
    ADMYR,
    EMPLOY,
    PRIMINC,
    DETNLF
FROM teds_a_raw_2015_2019;
'''

create_legal_info = '''
CREATE TABLE IF NOT EXISTS LegalInfo AS
SELECT
    CASEID,
    ADMYR,
    LIVARAG,
    ARRESTS,
    DETCRIM
FROM teds_a_raw_2015_2019;
'''

create_substance_use_history = '''
CREATE TABLE IF NOT EXISTS SubstanceUseHistory AS
SELECT
    CASEID,
    ADMYR,
    SUB1,
    ROUTE1,
    FREQ1,
    FRSTUSE1,
    SUB2,
    ROUTE2,
    FREQ2,
    FRSTUSE2,
    SUB3,
    ROUTE3,
    FREQ3,
    FRSTUSE3,
    IDU,
    ALCFLG,
    COKEFLG,
    MARFLG,
    HERFLG,
    METHFLG,
    OPSYNFLG,
    PCPFLG,
    HALLFLG,
    MTHAMFLG,
    AMPHFLG,
    STIMFLG,
    BENZFLG,
    TRNQFLG,
    BARBFLG,
    SEDHPFLG,
    INHFLG,
    OTCFLG,
    OTHERFLG
FROM teds_a_raw_2015_2019;
'''

create_treatment_information = '''
CREATE TABLE IF NOT EXISTS TreatmentInformation AS
SELECT
    CASEID,
    ADMYR,
    SERVICES,
    METHUSE,
    PRIMPAY,
    DAYWAIT,
    PSOURCE,
    NOPRIOR,
    FREQ_ATND_SELF_HELP,
    DSMCRIT,
    ALCDRUG,
    HLTHINS,
    PSYPROB
FROM teds_a_raw_2015_2019;
'''

# Execute the queries
dbcon.execute(create_demographics)
dbcon.execute(create_employment_details)
dbcon.execute(create_legal_info)
dbcon.execute(create_substance_use_history)
dbcon.execute(create_treatment_information)
dbcon.close()


