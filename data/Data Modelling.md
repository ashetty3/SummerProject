# Data Modelling 

### Considerations
* Dimension Tables: These tables store descriptive attributes (qualitative data) and are used to describe dimensions of your facts. in this case we have a lot of individual health, demographics and treatment/service descriptions avialable. 
* Fact Tables: These tables store quantitative data or events and are typically where the numeric data related to business processes are stored. In this scenario it's mainly factors originating from date-visited for admission and various layers of granualrity about substance use history. The fact table might just look like the admission log.
* Relationships: Establish proper foreign key relationships between dimension and fact tables. CASE-ID and ADM-YR are a unique combination in the data 

### Assumptions -- IMPORTANT NOTE
An important caveat for the data is that repeat admissions of the same patient may or may not be captured. since this is a practice data set I might generate some mock data here for learning purposes. 

### Normalization 

#### First Normal Form (1NF)
* Definition: Ensures that the table has only atomic (indivisible) values, and each column contains only one value per record.
* Application: All tables ensure that each column contains only a single value and each record is unique (e.g., each CASEID is unique).

#### Second Normal Form (2NF)
* Definition: Ensures that the table is in 1NF and that all non-key attributes are fully functionally dependent on the entire primary key.
* Application: For example, in the SubstanceUseHistory table, all columns depend on the combination of CASEID and ADMYR. Similarly, in TreatmentInformation, all columns depend on the primary key (CASEID, ADMYR).

#### Third Normal Form (3NF)
* Definition: Ensures that the table is in 2NF and that all the attributes are only dependent on the primary key, not on other non-key attributes (no transitive dependencies).
* Application: For example, in the Demographic attributes were separated into Demographics, EmploymentDetails, and LegalInfo tables to ensure that each non-key attribute is directly dependent on the primary key.

## Table Definitions


## 1. Demographics (Dimension Table)
- **CASEID**: Case identification number
- **ADMYR**: Year of admission
- **AGE**: Age at admission
- **GENDER**: Gender
- **RACE**: Race
- **ETHNIC**: Ethnicity
- **MARSTAT**: Marital status
- **EDUC**: Education
- **PREG**: Pregnant at admission
- **VET**: Veteran status
- **STFIPS**: Census state FIPS code
- **CBSA2010**: CBSA 2010 code
- **REGION**: Census region
- **DIVISION**: Census division

## 3. EmploymentDetails (Dimension Table)
- **CASEID**: Case identification number
- **ADMYR**: Year of admission
- **EMPLOY**: Employment status
- **PRIMINC**: Source of income/support
- **DETNLF**: Detailed not in labor force


## 4. LegalInfo (Dimension Table)
- **CASEID**: Case identification number
- **ADMYR**: Year of admission
- **LIVARAG**: Living arrangements
- **ARRESTS**: Arrests in past 30 days
- **DETCRIM**: Detailed criminal justice referral

## 5. Substance Use History (Fact Table)
- **CASEID**: Case identification number
- **ADMYR**: Year of admission
- **SUB1**: Substance use (primary)
- **ROUTE1**: Route of administration (primary)
- **FREQ1**: Frequency of use (primary)
- **FRSTUSE1**: Age at first use (primary)
- **SUB2**: Substance use (secondary)
- **ROUTE2**: Route of administration (secondary)
- **FREQ2**: Frequency of use (secondary)
- **FRSTUSE2**: Age at first use (secondary)
- **SUB3**: Substance use (tertiary)
- **ROUTE3**: Route of administration (tertiary)
- **FREQ3**: Frequency of use (tertiary)
- **FRSTUSE3**: Age at first use (tertiary)
- **IDU**: Current IV drug use reported at admission
- **ALCFLG**: Alcohol reported at admission
- **COKEFLG**: Cocaine/crack reported at admission
- **MARFLG**: Marijuana/hashish reported at admission
- **HERFLG**: Heroin reported at admission
- **METHFLG**: Non-rx methadone reported at admission
- **OPSYNFLG**: Other opiates/synthetics reported at admission
- **PCPFLG**: PCP reported at admission
- **HALLFLG**: Hallucinogens reported at admission
- **MTHAMFLG**: Methamphetamine/speed reported at admission
- **AMPHFLG**: Other amphetamines reported at admission
- **STIMFLG**: Other stimulants reported at admission
- **BENZFLG**: Benzodiazepines reported at admission
- **TRNQFLG**: Other tranquilizers reported at admission
- **BARBFLG**: Barbiturates reported at admission
- **SEDHPFLG**: Other sedatives/hypnotics reported at admission
- **INHFLG**: Inhalants reported at admission
- **OTCFLG**: Over-the-counter medication reported at admission
- **OTHERFLG**: Other drug reported at admission

## 6. Treatment Information (Fact Table)
- **CASEID**: Case identification number
- **ADMYR**: Year of admission
- **SERVICES**: Type of treatment service/setting
- **METHUSE**: Medication-assisted opioid therapy
- **PRIMPAY**: Primary source of payment for treatment
- **DAYWAIT**: Days waiting to enter substance use treatment
- **PSOURCE**: Referral source
- **NOPRIOR**: Previous substance use treatment episodes
- **FREQ_ATND_SELF_HELP**: Frequency of attendance at self-help groups
- **DSMCRIT**: DSM diagnosis (SuDS 4 or SuDS 19)
- **ALCDRUG**: Substance use type
- **HLTHINS**: Health insurance
- **PSYPROB**: Co-occurring mental and substance use disorders
- **DSMCRIT**: DSM diagnosis (SuDS 4 or SuDS 19)
