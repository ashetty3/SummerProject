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

# SQL script to create and populate the DemographicValueLabelMapping table with auto-generated ID and date added

create_mapping_table = '''

CREATE SEQUENCE IF NOT EXISTS serial_map;

CREATE TABLE IF NOT EXISTS ValueLabelMapping (
    id INTEGER DEFAULT NEXTVAL('serial_map') PRIMARY KEY, -- SERIAL OR AUTO_INCREMENT COULD WORK IN REAL SQL BUT NOT DUCKDB
    value INT,
    label VARCHAR,
    tablename VARCHAR,
    date_added DATE DEFAULT CURRENT_DATE
);

INSERT INTO ValueLabelMapping (value, label, tablename) VALUES
-- AGE
(1, '12–14 years', 'AGE'),
(2, '15–17 years', 'AGE'),
(3, '18–20 years', 'AGE'),
(4, '21–24 years', 'AGE'),
(5, '25–29 years', 'AGE'),
(6, '30–34 years', 'AGE'),
(7, '35–39 years', 'AGE'),
(8, '40–44 years', 'AGE'),
(9, '45–49 years', 'AGE'),
(10, '50–54 years', 'AGE'),
(11, '55–64 years', 'AGE'),
(12, '65 years and older', 'AGE'),

-- GENDER
(1, 'Male', 'GENDER'),
(2, 'Female', 'GENDER'),
(-9, 'Missing/unknown/not collected/invalid', 'GENDER'),

-- RACE
(1, 'Alaska Native (Aleut, Eskimo, Indian)', 'RACE'),
(2, 'American Indian (other than Alaska Native)', 'RACE'),
(3, 'Asian or Pacific Islander', 'RACE'),
(4, 'Black or African American', 'RACE'),
(5, 'White', 'RACE'),
(6, 'Asian', 'RACE'),
(7, 'Other single race', 'RACE'),
(8, 'Two or more races', 'RACE'),
(9, 'Native Hawaiian or Other Pacific Islander', 'RACE'),
(-9, 'Missing/unknown/not collected/invalid', 'RACE'),

-- ETHNIC
(1, 'Puerto Rican', 'ETHNIC'),
(2, 'Mexican', 'ETHNIC'),
(3, 'Cuban or other specific Hispanic', 'ETHNIC'),
(4, 'Not of Hispanic or Latino origin', 'ETHNIC'),
(5, 'Hispanic or Latino, specific origin not specified', 'ETHNIC'),
(-9, 'Missing/unknown/not collected/invalid', 'ETHNIC'),

-- MARSTAT
(1, 'Never married', 'MARSTAT'),
(2, 'Now married', 'MARSTAT'),
(3, 'Separated', 'MARSTAT'),
(4, 'Divorced', 'MARSTAT'),
(5, 'Widowed', 'MARSTAT'),
(-9, 'Missing/unknown/not collected/invalid', 'MARSTAT'),

-- EMPLOY
(1, 'Full-time', 'EMPLOY'),
(2, 'Part-time', 'EMPLOY'),
(3, 'Unemployed', 'EMPLOY'),
(4, 'Not in labor force', 'EMPLOY'),
(-9, 'Missing/unknown/not collected/invalid', 'EMPLOY'),

-- DETNLF
(1, 'Homemaker', 'DETNLF'),
(2, 'Student', 'DETNLF'),
(3, 'Retired, disabled', 'DETNLF'),
(4, 'Resident of institution', 'DETNLF'),
(5, 'Other', 'DETNLF'),
(-9, 'Missing/unknown/not collected/invalid', 'DETNLF'),

-- PREG
(1, 'Yes', 'PREG'),
(2, 'No', 'PREG'),
(-9, 'Missing/unknown/not collected/invalid', 'PREG'),

-- VET
(1, 'Yes', 'VET'),
(2, 'No', 'VET'),
(-9, 'Missing/unknown/not collected/invalid', 'VET');

'''

# Execute the queries
dbcon.execute(create_demographics)
dbcon.execute(create_employment_details)
dbcon.execute(create_legal_info)
dbcon.execute(create_substance_use_history)
dbcon.execute(create_treatment_information)
dbcon.execute(create_mapping_table)
dbcon.close()


